import pytest

from pathfinder_network.datamodel.non_empty_string import NonEmptyString
from pathfinder_network.datamodel.string import String


def test_non_empty_string_valid():
    # Test that creating a NonEmptyString with a non-empty string works
    value = "test string"
    assert NonEmptyString(__root__=value) == "test string"


def test_non_empty_string_comparison_on_base_string_type():
    # Test that creating a NonEmptyString with a non-empty string works
    value = "test string"
    assert NonEmptyString(__root__=value) == String(__root__=value)


def test_non_empty_string_empty():
    # Test that creating NonEmptyString with an empty string raises ValueError
    with pytest.raises(ValueError, match="__root__ must not be empty"):
        NonEmptyString(__root__="")
