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
from pathfinder_network.datamodel.percent import Percent
from pathfinder_network.datamodel.string import String


@pytest.fixture(scope="session")
def valid_datetime():
    return DateTime(value="2022-04-01T12:00:00Z")


@pytest.fixture(scope="session")
def valid_carbon_footprint():
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

    return carbon_footprint
