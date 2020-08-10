import pytest

from zib_uploader.fetch_data import OntologyMappingsFetcher, OntologyMapping


@pytest.mark.integration_test
def test_class_mapping_fetcher_integrated():
    fetcher = OntologyMappingsFetcher(pagesize=1)
    mapping = next(fetcher.fetch())
    assert type(mapping) is OntologyMapping
