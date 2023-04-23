from pydantic import BaseModel, validator

from pathfinder_network.datamodel.emission_factor_ds import EmissionFactorDS


class EmissionFactorDSSet(BaseModel):
    """
    A set of EmissionFactorDSs of size 1 or larger.

    Attributes:
        datasets (list[EmissionFactorDS]): A list of EmissionFactorDS objects.

    Raises:
        ValueError: If the list of datasets is empty.
    """

    datasets: list[EmissionFactorDS]

    @validator("datasets")
    def check_datasets(cls, v: list[EmissionFactorDS]) -> list[EmissionFactorDS]:
        if len(v) < 1:
            raise ValueError(
                "EmissionFactorDSSet must contain at least one EmissionFactorDS"
            )
        return v
