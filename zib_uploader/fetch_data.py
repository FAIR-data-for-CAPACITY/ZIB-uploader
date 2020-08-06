from collections import namedtuple

import requests
from tqdm import tqdm

ATC_MAPPINGS_URL = 'http://data.bioontology.org/ontologies/ATC/mappings'
BIOPORTAL_API_KEY = '8b5b7825-538d-40e0-9e9e-5ab9274a9aeb'

AtcClassMapping = namedtuple('AtcClassMapping',
                             ['source', 'atc_class', 'mapped_class'])
AtcClassMapping.__doc__ = """
Mapping of ATC ontology class to another ontology class

Args:
    source (str): Source of the mapping
    atc_class (str): ATC class URI
    mapped_class (str): corresponding class in other ontology URI
"""


class AtcClassMappingsFetcher:
    """
    Fetch ATC ontology to other ontology class mappings from bioportal.
    """
    def __init__(self, pagesize=5000):
        self.pagesize = pagesize

    def _get(self, url: str):
        result = requests.get(url,
                              params={'apikey': BIOPORTAL_API_KEY,
                                      'display_links': 'false',
                                      'display_context': 'false',
                                      'pagesize': self.pagesize})
        return result.json()

    def _paginator(self):
        page = self._get(url=ATC_MAPPINGS_URL)
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
            yield AtcClassMapping(source=source,
                                  atc_class=mapping['classes'][0]['@id'],
                                  mapped_class=mapping['classes'][1]['@id'])

    def fetch(self):
        """
        Fetch ATC ontology to other ontology class mappings from bioportal.
        This loads around 250000 mapping pairs, so it can take around 5 minutes.

        Yields:
            AtcClassMapping namedtuples
        """
        for page in self._paginator():
            yield from self._get_mappings_from_page(page)
