import itertools
import logging

import click
from rdflib import Graph, URIRef

from zib_uploader.fetch_data import OntologyMappingsFetcher
from zib_uploader.process_data import OntologyMappingsProcessor

logger = logging.getLogger(__name__)


@click.command()
@click.argument('output_filepath', type=click.Path())
def main(output_filepath):
    """
    Fetch ATC ontology mappings from bioportal, process them, and write to
    ttl format. (Serves as example on how to chain OntologyMappingsFetcher and
    OntologyMappingsProcessor)
    """
    fetcher = OntologyMappingsFetcher()
    processor = OntologyMappingsProcessor()
    data = itertools.islice(fetcher.fetch())
    data = processor.process(data)
    g = Graph()
    for s, p, o in data:
        g.add((URIRef(s), URIRef(p), URIRef(o)))
    logger.info(f'Writing ontology mappings to {output_filepath}')
    g.serialize(output_filepath, format='turtle')


if __name__ == '__main__':
    logging.basicConfig(level='INFO')
    main()
