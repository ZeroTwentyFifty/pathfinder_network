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


def test_carbon_footprint_all_mandatory_fields():
    cross_sectoral_standards = CrossSectoralStandardSet(
        standards=[CrossSectoralStandard.ISO_STANDARD_14067]
    )

    carbon_footprint = CarbonFootprint(
        declared_unit=DeclaredUnit.kilogram,
        unitary_product_amount=Decimal(value=12),
        pcf_excluding_biogenic=Decimal(value=35),
        fossil_ghg_emissions=Decimal(value=100),
        fossil_carbon_content=Decimal(value=65),
        biogenic_carbon_content=Decimal(value=8),
        characterization_factors=String(__root__="blah"),
        cross_sectoral_standards_used=cross_sectoral_standards,
        boundary_processes_description=String(__root__="bleep"),
        reference_period_start=DateTime(value="2023-04-01T12:00:00Z"),
        reference_period_end=DateTime(value="2024-04-01T12:00:00Z"),
        exempted_emissions_percent=Percent(value=42),
        exempted_emissions_description=String(__root__="hello"),
        packaging_emissions_included=False,
    )

    assert carbon_footprint.declared_unit == "kilogram"
