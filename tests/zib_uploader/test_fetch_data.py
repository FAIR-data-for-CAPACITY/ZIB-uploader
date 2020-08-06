import pytest

from zib_uploader.fetch_data import AtcClassMappingsFetcher, AtcClassMapping


@pytest.mark.integration_test
def test_atc_class_mapping_fetcher_integrated():
    fetcher = AtcClassMappingsFetcher(pagesize=1)
    mapping = next(fetcher.fetch())
    assert type(mapping) is AtcClassMapping
