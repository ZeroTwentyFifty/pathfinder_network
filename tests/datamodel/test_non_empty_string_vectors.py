import pytest

from pathfinder_network.datamodel.non_empty_string import NonEmptyString
from pathfinder_network.datamodel.non_empty_string_vector import (
    NonEmptyStringVector,
)


def test_non_empty_string_vector_with_valid_non_empty_strings():
    strings = [
        NonEmptyString(value="this is the first string"),
        NonEmptyString(value="and this one, this is the second string"),
        NonEmptyString(value="and are you ready for the third string?"),
    ]
    non_empty_string_vector = NonEmptyStringVector(non_empty_strings=strings)
    assert non_empty_string_vector.non_empty_strings == strings


def test_non_empty_string_vector_with_valid_strings():
    strings = [
        "this is the first string",
        "and this one, this is the second string",
        "and are you ready for the third string?",
    ]
    on_empty_string_vector = NonEmptyStringVector(non_empty_strings=strings)
    assert str(on_empty_string_vector) == f"[{', '.join(map(str, strings))}]"


def test_non_empty_string_vector_with_empty_list():
    with pytest.raises(
        ValueError,
        match="NonEmptyStringVector must contain at least one NonEmptyString",
    ):
        NonEmptyStringVector(non_empty_strings=[])
