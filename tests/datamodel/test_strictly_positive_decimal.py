from decimal import Decimal

import pytest

from pathfinder_network.datamodel.strictly_positive_decimal import (
    StrictlyPositiveDecimal,
)


def test_valid_values():
    # test with Decimal object
    spd = StrictlyPositiveDecimal(value=Decimal("0.123"))
    assert str(spd) == "0.123"
    assert repr(spd) == "StrictlyPositiveDecimal(value=0.123)"

    # test with float
    spd = StrictlyPositiveDecimal(value=0.123)
    assert str(spd) == "0.123"
    assert repr(spd) == "StrictlyPositiveDecimal(value=0.123)"

    # test with integer
    spd = StrictlyPositiveDecimal(value=1000)
    assert str(spd) == "1000"
    assert repr(spd) == "StrictlyPositiveDecimal(value=1000)"

    # test with string
    spd = StrictlyPositiveDecimal(value="42.102340")
    assert str(spd) == "42.102340"
    assert repr(spd) == "StrictlyPositiveDecimal(value=42.102340)"


def test_invalid_values():
    # test with zero value
    with pytest.raises(ValueError):
        StrictlyPositiveDecimal(value=0)

    # test with negative value
    with pytest.raises(ValueError):
        StrictlyPositiveDecimal(value=-0.123)

    # test with string containing negative value
    with pytest.raises(ValueError):
        StrictlyPositiveDecimal(value="-42.102340")

    # test with non-numeric string
    with pytest.raises(ValueError):
        StrictlyPositiveDecimal(value="invalid value")
