from pydantic import BaseModel, validator

from pathfinder_network.datamodel.cross_sectoral_standard import CrossSectoralStandard


class CrossSectoralStandardSet(BaseModel):
    """
    A set of CrossSectoralStandards of size 1 or larger.

    Attributes:
        standards (list[CrossSectoralStandard]): A list of CrossSectoralStandard objects.

    Raises:
        ValueError: If the list of standards is empty.
    """

    standards: list[CrossSectoralStandard]

    @validator("standards")
    def check_rules(cls, v: list[CrossSectoralStandard]) -> list[CrossSectoralStandard]:
        if len(v) < 1:
            raise ValueError(
                "CrossSectoralStandardSet must contain at least one CrossSectoralStandard"
            )
        return v
