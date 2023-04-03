import pytest
from pydantic import ValidationError

from pathfinder_network.datamodel.urn import URN


def test_valid_urn():
    value = "urn:example:foo-bar:baz-qux:1234"
    urn = URN(value=value)
    assert urn.value == value


def test_invalid_urn():
    with pytest.raises(ValidationError):
        value = "not_an_urn"
        URN(value=value)
