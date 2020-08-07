#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the zib_uploader module.
"""
import itertools
import logging

import pytest

from zib_uploader.fetch_data import OntologyMapping, OntologyMappingsFetcher
from zib_uploader.zib_uploader import OntologyMappingsProcessor

logging.basicConfig(level=logging.DEBUG)


class TestOntologyMappingsProcessor:
    test_source = 'SOURCE'
    test_mapping = OntologyMapping(source=test_source,
                                   classes=('class1', 'class2'))

    def test_to_rdf(self):
        test_mapping_stream = [self.test_mapping]
        test_predicate = 'test_predicate'
        processor = OntologyMappingsProcessor(valid_sources=(self.test_source,),
                                              predicate=test_predicate)
        result = list(processor.process(test_mapping_stream))
        assert len(result) == 2  # two rdf triples per mapping (bidirectional)
        for s, p, o in result:
            assert s in self.test_mapping.classes
            assert o in self.test_mapping.classes
            assert s != o
            assert p == test_predicate

    def test_drop_duplicates(self):
        # duplicates in data
        test_mapping_stream = [self.test_mapping, self.test_mapping]
        processor = OntologyMappingsProcessor(valid_sources=(self.test_source,),
                                              drop_duplicates=True)
        result = list(processor.process(test_mapping_stream))
        assert len(result) == 2  # two rdf triples per mapping (bidirectional)

    def test_filter_sources(self):
        test_invalid_mapping = OntologyMapping(source='INVALID_SOURCE',
                                               classes=('invalid_class1',
                                                        'invalid_class2'))
        test_mapping_stream = [self.test_mapping, test_invalid_mapping]
        processor = OntologyMappingsProcessor(valid_sources=(self.test_source,))
        result = list(processor.process(test_mapping_stream))
        assert len(result) == 2  # two rdf triples per mapping (bidirectional)
        for s, p, o in result:
            assert s in self.test_mapping.classes
            assert o in self.test_mapping.classes

    @pytest.mark.integration_test
    def test_integrated_on_bioportal_data(self):
        fetcher = OntologyMappingsFetcher(pagesize=5)
        data = itertools.islice(fetcher.fetch(), 5)
        processor = OntologyMappingsProcessor()
        result = list(processor.process(data))
        assert result
