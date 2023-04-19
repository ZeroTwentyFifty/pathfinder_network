from pydantic import ValidationError
from pytest import raises

from pathfinder_network.datamodel.string import String


def test_valid_string():
    # Test valid strings
    s1 = String(__root__="Hello, World!")
    assert s1 == "Hello, World!"
    s2 = String(__root__="1234")
    assert s2 == "1234"
    s3 = String(__root__="🐍 is the best")
    assert s3 == "🐍 is the best"


def test_empty_string():
    empty_string = String(__root__="")
    assert empty_string == ""


def test_other_types():
    s1 = String(__root__=123)
    assert s1 == "123"
    s2 = String(__root__=0.0001)
    assert s2 == "0.0001"


def test_none_string():
    # Test None string
    with raises(ValidationError):
        String(__root__=None)
