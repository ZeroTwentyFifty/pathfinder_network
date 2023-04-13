from enum import Enum


class ProductOrSectorSpecificRuleOperator(str, Enum):
    """
    Enumeration of Product Category Rule (PCR) operators.
    Valid values are:
    - PEF: for EU / PEF Methodology PCRs
    - EPD International: for PCRs authored or published by EPD International
    - Other: for a PCR not published by the operators mentioned above
    """

    PEF = "PEF"
    EPD_INTERNATIONAL = "EPD International"
    OTHER = "Other"
