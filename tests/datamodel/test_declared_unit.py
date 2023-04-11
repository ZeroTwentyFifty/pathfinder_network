import pytest

from pathfinder_network.datamodel.declared_unit import DeclaredUnit


def test_valid_units():
    valid_units = [
        "liter",
        "kilogram",
        "cubic meter",
        "kilowatt hour",
        "megajoule",
        "ton kilometer",
        "square meter",
    ]
    for unit in valid_units:
        assert DeclaredUnit(unit).value == unit


def test_invalid_unit():
    with pytest.raises(ValueError):
        DeclaredUnit("invalid unit")
