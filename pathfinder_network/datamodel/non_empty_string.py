from pydantic import validator

from pathfinder_network.datamodel.string import String


class NonEmptyString(String):
    """
    A String with 1 or more characters.
    """

    @validator("value")
    def value_must_not_be_empty(cls, v: str) -> str:
        if not v:
            raise ValueError("value must not be empty")
        return v
