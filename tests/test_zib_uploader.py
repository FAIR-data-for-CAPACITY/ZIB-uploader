#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the zib_uploader module.
"""
import pytest

from zib_uploader import zib_uploader


def test_something():
    assert True


def test_with_error():
    with pytest.raises(ValueError):
        # Do something that raises a ValueError
        raise(ValueError)


# Fixture example
@pytest.fixture
def an_object():
    return {}


def test_zib_uploader(an_object):
    assert an_object == {}
