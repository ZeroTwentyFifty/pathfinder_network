from pydantic import ValidationError
from pytest import raises

from pathfinder_network.datamodel.string import String


def test_valid_string():
    # Test valid strings
    s1 = String(value="Hello, World!")
    assert str(s1) == "Hello, World!"
    s2 = String(value="1234")
    assert str(s2) == "1234"
    s3 = String(value="🐍 is the best")
    assert str(s3) == "🐍 is the best"


def test_empty_string():
    empty_string = String(value="")
    assert str(empty_string) == ""


def test_other_types():
    s1 = String(value=123)
    assert str(s1) == "123"
    s2 = String(value=0.0001)
    assert str(s2) == "0.0001"


def test_none_string():
    # Test None string
    with raises(ValidationError):
        String(value=None)
