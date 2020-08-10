# -*- coding: utf-8 -*-"""Documentation about the ZIB uploader module."""
import logging
from typing import Iterator, Tuple

import pandas as pd

from zib_uploader.fetch_data import OntologyMapping

logger = logging.getLogger(__name__)

DEFAULT_MAPPING_PREDICATE = 'http://www.w3.org/2004/02/skos/core#closeMatch'
DEFAULT_VALID_SOURCES = ('CUI',)


class OntologyMappingsProcessor:
    """
    Process ontology mappings: (1) (optionally) filter out exact
    duplicates(same source, same classes mapped, probably we are missing
    some annotation of the mappings here), (2) filter out mappings with
    invalid sources, (3) transform mappings into RDF triples
    """
    def __init__(self, predicate: str = DEFAULT_MAPPING_PREDICATE,
                 valid_sources: Tuple[str] = DEFAULT_VALID_SOURCES,
                 drop_duplicates: bool = True):
        """
        Args:
            predicate (str): the predicate that should be ascribed to the
                mapped classes.
            valid_sources (tuple[str]): valid sources of mappings. In the ATC
                mappings these are: CUI, LOOM, and SAME_URI
            drop_duplicates (bool): Toggle dropping duplicates

        """
        self.predicate = predicate
        self.valid_sources = valid_sources
        self.drop_duplicates = drop_duplicates

    def _filter(self, mappings_df: pd.DataFrame):
        """
        Drop duplicate mappings and mappings with invalid sources.
        """
        # drop duplicate mappings
        if self.drop_duplicates:
            len_before = len(mappings_df)
            mappings_df = mappings_df.drop_duplicates()
            num_dropped = len_before - len(mappings_df)
            logger.info(f'Dropped {num_dropped} duplicates out of {len_before}')

        # drop mappings with invalid sources
        len_before = len(mappings_df)
        has_valid_source = mappings_df['source'].isin(self.valid_sources)
        mappings_df = mappings_df[has_valid_source]
        num_dropped = len_before - len(mappings_df)
        logger.info(f'Dropped {num_dropped} out of {len_before} mappings with '
                    f'invalid source')
        return mappings_df

    def _to_rdf(self, mappings_df: pd.DataFrame) -> Iterator[Tuple]:
        logger.info(f'Converting {len(mappings_df)} mappings to RDF triples')
        for _, (source, classes) in mappings_df.iterrows():
            yield classes[0], self.predicate, classes[1]
            yield classes[1], self.predicate, classes[0]

    def process(self, mapping_stream: Iterator[OntologyMapping]
                ) -> Iterator[Tuple]:
        """
        Process a stream of ontology mappings. Filter and transform into RDF
        triples.

        Args:
            mapping_stream: ontology mapping input

        Yields:
            rdf triples describing the mapping
        """
        mappings_df = pd.DataFrame(mapping_stream)
        mappings_df = self._filter(mappings_df)
        return self._to_rdf(mappings_df)
