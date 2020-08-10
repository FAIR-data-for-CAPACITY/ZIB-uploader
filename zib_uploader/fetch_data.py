import logging
import os
from collections import namedtuple
from typing import Iterator

import requests
from tqdm import tqdm

logger = logging.getLogger(__name__)

ATC_MAPPINGS_URL = 'http://data.bioontology.org/ontologies/ATC/mappings'
DEFAULT_PAGESIZE = 5000
BIOPORTAL_API_KEY = os.environ.get('BIOPORTAL_API_KEY')

OntologyMapping = namedtuple('OntologyMapping', ['source', 'classes'])
OntologyMapping.__doc__ = """
Mapping of ontology class to another ontology class

Args:
    source (str): Source of the mapping
    classes (size 2 tuple if strings): URIs of classes that are mapped to each
        other
"""


class OntologyMappingsFetcher:
    """
    Fetch ontology to other ontology class mappings from bioportal.
    """
    def __init__(self, url=ATC_MAPPINGS_URL, pagesize=DEFAULT_PAGESIZE):
        """
        Args:
            url (str): Url pointing to bioportal mappings, default is ATC
                mappings
            pagesize (int): Define pagesize when paginating
        """
        self.url = url
        self.pagesize = pagesize

    def _get(self, url: str):
        result = requests.get(url,
                              params={'apikey': BIOPORTAL_API_KEY,
                                      'display_links': 'false',
                                      'display_context': 'false',
                                      'pagesize': self.pagesize})
        return result.json()

    def _paginator(self):
        page = self._get(url=self.url)
        yield page
        progress_bar = tqdm(total=page['pageCount'])
        while page['links']['nextPage'] is not None:
            progress_bar.update(1)
            page = self._get(page['links']['nextPage'])
            yield page

    @staticmethod
    def _get_mappings_from_page(page):
        for mapping in page['collection']:
            source = mapping['source']
            yield OntologyMapping(source=source,
                                  classes=(mapping['classes'][0]['@id'],
                                                mapping['classes'][1]['@id']))

    def fetch(self) -> Iterator[OntologyMapping]:
        """
        Fetch ontology to other ontology class mappings from bioportal.
        For ATC this loads around 250000 mapping pairs, so it can take around 5
        minutes. For other mappings it could possibly take even longer.

        Yields:
            OntologyMapping namedtuples
        """
        logger.info(f'Fetching ontology mappings from {self.url}, can take '
                    f'several minutes')
        for page in self._paginator():
            yield from self._get_mappings_from_page(page)
