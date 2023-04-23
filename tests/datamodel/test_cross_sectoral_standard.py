import pytest

from pathfinder_network.datamodel.cross_sectoral_standard import CrossSectoralStandard


def test_valid_cross_sectoral_standards():
    valid_cs_standards = [
        "GHG Protocol Product standard",
        "ISO Standard 14067",
        "ISO Standard 14044",
    ]
    for cs_standard in valid_cs_standards:
        assert CrossSectoralStandard(cs_standard).value == cs_standard


def test_cross_sectoral_standards_values():
    assert CrossSectoralStandard.GHG_PROTOCOL == "GHG Protocol Product standard"
    assert CrossSectoralStandard.ISO_STANDARD_14067 == "ISO Standard 14067"
    assert CrossSectoralStandard.ISO_STANDARD_14044 == "ISO Standard 14044"


def test_invalid_cross_sectoral_standard():
    with pytest.raises(ValueError):
        CrossSectoralStandard("invalid unit")
