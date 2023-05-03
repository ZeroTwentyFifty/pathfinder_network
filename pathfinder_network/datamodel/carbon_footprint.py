from enum import Enum

from pydantic import BaseModel

from pathfinder_network.datamodel.assurance import Assurance
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


class BiogenicAccountingMethodology(str, Enum):
    """
    BiogenicAccountingMethodology is the enumeration of the standard followed to account for biogenic emissions and
    removals.

    Valid values are:

    - PEF (str): EU Product Environmental Footprint Guide
    - ISO (str): ISO Standard 14067
    - GHPG (str): Greenhouse Gas Protocol (GHGP) Land sector and Removals Guidance
    - Quantis (str): Quantis Accounting for Natural Climate Solutions Guidance
    """

    PEF = "PEF"
    ISO = "ISO"
    GHGP = "GHPG"
    QUANTIS = "Quantis"


class CarbonFootprint(BaseModel):
    """
    Data type Assurance contains the assurance in conformance with Pathfinder Framework chapter 5 and appendix B.

    Attributes:
        declared_unit (DeclaredUnit): The unit of analysis of the product.
        unitary_product_amount (Decimal): The amount of Declared Units contained within the product to which the PCF is referring to.
            The value MUST be strictly greater than 0.
        pcf_excluding_biogenic (Decimal): The product carbon footprint of the product excluding biogenic emissions.
            The value MUST be calculated per declared unit with unit kg of CO2 equivalent per declared unit (kgCO2e / declaredUnit),
            expressed as a decimal equal to or greater than zero.
        pcf_including_biogenic (Decimal): If present, the product carbon footprint of the product including biogenic emissions.
            The value MUST be calculated per declared unit with unit kg of CO2 equivalent per declared unit (kgCO2e / declaredUnit),
            expressed as a decimal.
            NOTE: the value of this property can be less than 0 (zero).
        fossil_ghg_emissions (Decimal): The emissions from the combustion of fossil sources.
            The value MUST be calculated per declared unit with unit kg of CO2 equivalent per declared unit (kgCO2e / declaredUnit),
            expressed as a decimal equal to or greater than zero.
        fossil_carbon_content (Decimal): The fossil carbon amount embodied in the product.
            The value MUST be calculated per declared unit with unit kg of CO2 equivalent per declared unit (kgCO2e / declaredUnit),
            expressed as a decimal equal to or greater than zero.
        biogenic_carbon_content (Decimal): The biogenic carbon amount embodied in the product.
            The value MUST be calculated per declared unit with unit kg of CO2 equivalent per declared unit (kgCO2e / declaredUnit),
            expressed as a decimal equal to or greater than zero.
        dluc_ghg_emissions (Decimal): If present, emissions resulting from recent (i.e., previous 20 years) carbon stock loss due to land conversion
            directly on the area of land under consideration. The value of this property MUST include direct land use change (dLUC) where available,
            otherwise statistical land use change (sLUC) can be used. The value MUST be calculated per declared unit with unit kg of CO2 equivalent
            per declared unit (kgCO2e / declaredUnit), expressed as a decimal equal to or greater than zero.
            See Pathfinder Framework (Appendix B) for details.
        land_management_ghg_emissions (Decimal): If present, GHG emissions and removals associated with land-management-related changes, including
            non-CO2 sources. The value MUST be calculated per declared unit with unit kg of CO2 equivalent per declared unit (kgCO2e / declaredUnit),
            expressed as a decimal equal to or greater than zero.
            NOTE: version 1 did not explicitly include non-CO2 sources. This is now included in the definition.
        other_biogenic_ghg_emissions (Decimal): If present, all other biogenic GHG emissions associated with product manufacturing and transport
            that are not included in dLUC (direct land use change) or landManagementGhgEmissions.
            The value MUST be calculated per declared unit with unit kg of CO2 equivalent per declared unit (kgCO2e / declaredUnit),
            expressed as a decimal equal to or greater than zero.
    """

    declared_unit: DeclaredUnit
    unitary_product_amount: Decimal
    pcf_excluding_biogenic: Decimal
    pcf_including_biogenic: Decimal | None = None
    fossil_ghg_emissions: Decimal
    fossil_carbon_content: Decimal
    biogenic_carbon_content: Decimal
    dluc_ghg_emissions: Decimal | None = None
    land_management_ghg_emissions: Decimal | None = None
    other_biogenic_ghg_emissions: Decimal | None = None
    iluc_ghg_emissions: Decimal | None = None
    biogenic_carbon_withdrawal: Decimal | None = None
    aircraft_ghg_emissions: Decimal | None = None
    characterization_factors: String
    cross_sectoral_standards_used: CrossSectoralStandardSet
    product_or_sector_specific_rules: ProductOrSectorSpecificRuleSet | None = None
    biogenic_accounting_methodology: BiogenicAccountingMethodology | None = None
    boundary_processes_description: String
    reference_period_start: DateTime
    reference_period_end: DateTime
    geography_country_subdivision: String | None = None
    geography_country: ISO3166CC | None = None
    geography_region_or_subregion: RegionOrSubregion | None = None
    secondary_emission_factor_sources: EmissionFactorDSSet | None = None
    exempted_emissions_percent: Percent
    exempted_emissions_description: String
    packaging_emissions_included: bool
    packaging_ghg_emissions: Decimal | None = None
    allocation_rules_description: String | None = None
    uncertainty_assessment_description: String | None = None
    primary_data_share: Percent | None = None
    assurance: Assurance | None = None
