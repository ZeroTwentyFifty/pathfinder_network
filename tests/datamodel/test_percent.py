import pytest

from pathfinder_network.datamodel.percent import Percent


def test_percent_valid_values():
    percent = Percent(value=0)
    assert str(percent) == "0"
    assert repr(percent) == "Percent(value=0)"

    percent = Percent(value=23.0)
    assert str(percent) == "23.0"
    assert repr(percent) == "Percent(value=23.0)"

    percent = Percent(value=7.183924)
    assert str(percent) == "7.183924"
    assert repr(percent) == "Percent(value=7.183924)"

    percent = Percent(value=100)
    assert str(percent) == "100"
    assert repr(percent) == "Percent(value=100)"


def test_percent_invalid_values():
    with pytest.raises(ValueError):
        Percent(value=-1)

    with pytest.raises(ValueError):
        Percent(value=101)

    with pytest.raises(ValueError):
        Percent(value=234.892031)
