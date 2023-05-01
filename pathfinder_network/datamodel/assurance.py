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
    """

    assurance: bool
