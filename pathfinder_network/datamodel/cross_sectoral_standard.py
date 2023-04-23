from enum import Enum


class CrossSectoralStandard(str, Enum):
    """
    CrossSectoralStandard is the enumeration of accounting standards used for product carbon footprint calculation.
    Valid values are:
    - GHG Protocol Product standard: for the GHG Protocol Product standard
    - ISO Standard 14067: for ISO Standard 14067
    - ISO Standard 14044: for ISO Standard 14044
    """

    GHG_PROTOCOL = "GHG Protocol Product standard"
    ISO_STANDARD_14067 = "ISO Standard 14067"
    ISO_STANDARD_14044 = "ISO Standard 14044"
