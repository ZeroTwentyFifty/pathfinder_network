from datetime import datetime
from enum import Enum

from pydantic import BaseModel

from pathfinder_network.datamodel.non_empty_string import NonEmptyString


class AssuranceCoverage(str, Enum):
    corporate_level = "corporate level"
    product_line = "product line"
    pcf_system = "PCF system"
    product_level = "product level"


class AssuranceLevel(str, Enum):
    limited = "limited"
    reasonable = "reasonable"


class AssuranceBoundary(str, Enum):
    gate_to_gate = "Gate-to-Gate"
    cradle_to_gate = "Cradle-to-Gate"


class Assurance(BaseModel):
    """
    Data type Assurance contains the assurance in conformance with Pathfinder Framework chapter 5 and appendix B.

    Attributes:
    - assurance (bool): Binary indicator stating whether the PCF has been assured in line with
    Pathfinder Framework requirements
    - coverage (str): Level of granularity of the emissions data assured. Valid values are:
        - "corporate level" for corporate level
        - "product line" for product line
        - "PCF system" for PCF System
        - "product level" for product level
        This property MAY be undefined if no assurance has taken place.
    - level (str): Level of assurance applicable to the PCF. Valid values are:
        - "limited" for limited assurance
        - "reasonable" for reasonable assurance
        This property is optional.
    - boundary (str): Boundary of the assurance. Valid values are:
        - "Gate-to-Gate" for Gate-to-Gate
        - "Cradle-to-Gate" for Cradle-to-Gate
        This property is optional.
    - providerName (str): The non-empty name of the independent third party engaged to undertake the assurance.
        This property is optional.
    - completedAt (datetime): The date at which the assurance was completed. This property is optional.
    - standardName (str): Name of the standard against which the PCF was assured. This property is optional.
    - comments (str): Any additional comments that will clarify the interpretation of the assurance.
        This property may be an empty string. This property is optional.
    """

    assurance: bool
    coverage: AssuranceCoverage | None = None
    level: AssuranceLevel | None = None
    boundary: AssuranceBoundary | None = None
    providerName: NonEmptyString | None = None
    completedAt: datetime | None = None
    standardName: str | None = None
    comments: str | None = None
