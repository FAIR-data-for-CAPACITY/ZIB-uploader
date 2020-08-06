import pytest

from zib_uploader.fetch_data import ClassMappingsFetcher, OntologyClassMapping


@pytest.mark.integration_test
def test_class_mapping_fetcher_integrated():
    fetcher = ClassMappingsFetcher(pagesize=1)
    mapping = next(fetcher.fetch())
    assert type(mapping) is OntologyClassMapping
