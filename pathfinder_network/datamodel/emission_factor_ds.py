from pydantic import BaseModel

from pathfinder_network.datamodel.non_empty_string import NonEmptyString


class EmissionFactorDS(BaseModel):
    """
    A reference to an emission factor database.

    Attributes:
        name (NonEmptyString): The non-empty name of the emission factor database.
        version (NonEmptyString): The non-empty version of the emission factor database.
    """

    name: NonEmptyString
    version: NonEmptyString
