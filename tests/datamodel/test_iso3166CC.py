import pytest
from pydantic import ValidationError

from pathfinder_network.datamodel.iso3166CC import ISO3166CC


@pytest.mark.parametrize("valid_value", ["US", "us"])
def test_valid_ISO3166CC(valid_value):
    iso_code = ISO3166CC(code=valid_value)
    assert iso_code.code == "US"


def test_invalid_ISO3166CC():
    with pytest.raises(ValueError):
        ISO3166CC(code="invalid")

    with pytest.raises(ValueError):
        ISO3166CC(code="US123")


@pytest.mark.parametrize("invalid_value", [None, [1, 2, 3], {"dict": "value"}])
def test_invalid_type_ISO3166CC(invalid_value):
    with pytest.raises(ValidationError):
        ISO3166CC(code=invalid_value)
