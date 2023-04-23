import pytest

from pathfinder_network.datamodel.cross_sectoral_standard import CrossSectoralStandard
from pathfinder_network.datamodel.cross_sectoral_standard_set import (
    CrossSectoralStandardSet,
)


@pytest.fixture
def valid_cross_sectoral_standard():
    standard = CrossSectoralStandard.ISO_STANDARD_14067

    return standard


def test_cross_sectoral_standard_set_with_valid_standard(valid_cross_sectoral_standard):
    csc_set = CrossSectoralStandardSet(standards=[valid_cross_sectoral_standard])
    assert csc_set.standards


def test_cross_sectoral_standard_set_with_empty_list():
    with pytest.raises(
        ValueError,
        match="CrossSectoralStandardSet must contain at least one CrossSectoralStandard",
    ):
        CrossSectoralStandardSet(standards=[])
