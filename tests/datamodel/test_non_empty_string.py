import pytest

from pathfinder_network.datamodel.non_empty_string import NonEmptyString


def test_non_empty_string_valid():
    # Test that creating a NonEmptyString with a non-empty string works
    value = "test string"
    assert NonEmptyString(value=value).value == value


def test_non_empty_string_empty():
    # Test that creating NonEmptyString with an empty string raises ValueError
    with pytest.raises(ValueError):
        NonEmptyString(value="")


def test_non_empty_string_none():
    # Test that creating a NonEmptyString with None raises a ValueError
    with pytest.raises(ValueError):
        NonEmptyString(value=None)
