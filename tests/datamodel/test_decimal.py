from decimal import Decimal as PyDecimal

import pytest
from pydantic import ValidationError

from pathfinder_network.datamodel.decimal import Decimal


def test_valid_decimal():
    d = Decimal(value=10)
    assert str(d) == "10"
    assert repr(d) == "Decimal(value=10)"

    d = Decimal(value=42.12)
    assert str(d) == "42.12"
    assert repr(d) == "Decimal(value=42.12)"

    d = Decimal(value=-182.84)
    assert str(d) == "-182.84"
    assert repr(d) == "Decimal(value=-182.84)"

    d = Decimal(value=PyDecimal("12345678901234567890.123456789"))
    assert str(d) == "12345678901234567890.123456789"
    assert repr(d) == "Decimal(value=12345678901234567890.123456789)"


@pytest.mark.parametrize(
    "invalid_value", ["hello", None, [1, 2, 3], "not a number"]
)
def test_invalid_decimal(invalid_value):
    with pytest.raises(ValidationError):
        Decimal(value=invalid_value)
