import datetime

import pytest

from pathfinder_network.datamodel.assurance import Assurance
from pathfinder_network.datamodel.carbon_footprint import (
    BiogenicAccountingMethodology,
    CarbonFootprint,
)
from pathfinder_network.datamodel.cross_sectoral_standard import CrossSectoralStandard
from pathfinder_network.datamodel.cross_sectoral_standard_set import (
    CrossSectoralStandardSet,
)
from pathfinder_network.datamodel.datetime import DateTime
from pathfinder_network.datamodel.decimal import Decimal
from pathfinder_network.datamodel.declared_unit import DeclaredUnit
from pathfinder_network.datamodel.emission_factor_ds_set import EmissionFactorDSSet
from pathfinder_network.datamodel.iso3166CC import ISO3166CC
from pathfinder_network.datamodel.percent import Percent
from pathfinder_network.datamodel.product_or_sector_specific_rule_set import (
    ProductOrSectorSpecificRuleSet,
)
from pathfinder_network.datamodel.region_or_subregion import RegionOrSubregion
from pathfinder_network.datamodel.string import String


def test_valid_biogenic_accounting_methodology():
    """Test that valid biogenic accounting methodologies are accepted"""
    assert BiogenicAccountingMethodology.PEF == "PEF"
    assert BiogenicAccountingMethodology.ISO == "ISO"
    assert BiogenicAccountingMethodology.GHGP == "GHPG"
    assert BiogenicAccountingMethodology.QUANTIS == "Quantis"


def test_invalid_biogenic_accounting_methodology():
    """Test that an invalid biogenic accounting methodology raises a ValueError"""
    with pytest.raises(ValueError):
        BiogenicAccountingMethodology("invalid")


def test_carbon_footprint_all_mandatory_fields(valid_carbon_footprint):
    assert valid_carbon_footprint.declared_unit == "kilogram"
