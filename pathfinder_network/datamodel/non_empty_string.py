from pydantic import validator

from pathfinder_network.datamodel.string import String


class NonEmptyString(String):
    """
    A String with 1 or more characters.
    """

    @validator("__root__")
    def value_must_not_be_empty(cls, v: str) -> str:
        if not v:
            raise ValueError("__root__ must not be empty")
        return v
