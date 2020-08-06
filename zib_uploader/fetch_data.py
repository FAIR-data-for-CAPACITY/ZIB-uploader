from collections import namedtuple
from typing import Iterator

import requests
from tqdm import tqdm

ATC_MAPPINGS_URL = 'http://data.bioontology.org/ontologies/ATC/mappings'
BIOPORTAL_API_KEY = '8b5b7825-538d-40e0-9e9e-5ab9274a9aeb'

OntologyClassMapping = namedtuple('OntologyClassMapping',
                                  ['source', 'classes'])
OntologyClassMapping.__doc__ = """
Mapping of ontology class to another ontology class

Args:
    source (str): Source of the mapping
    classes (size 2 tuple if strings): URIs of classes that are mapped to each
        other
"""


class ClassMappingsFetcher:
    """
    Fetch ontology to other ontology class mappings from bioportal.
    """
    def __init__(self, url=ATC_MAPPINGS_URL, pagesize=5000):
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
            yield OntologyClassMapping(source=source,
                                       classes=(mapping['classes'][0]['@id'],
                                                mapping['classes'][1]['@id']))

    def fetch(self) -> Iterator[OntologyClassMapping]:
        """
        Fetch ontology to other ontology class mappings from bioportal.
        For ATC this loads around 250000 mapping pairs, so it can take around 5
        minutes. For other mappings it could possibly take even longer.

        Yields:
            OntologyClassMapping namedtuples
        """
        for page in self._paginator():
            yield from self._get_mappings_from_page(page)
