from pydantic import BaseModel, validator

from pathfinder_network.datamodel.non_empty_string import NonEmptyString


class NonEmptyStringVector(BaseModel):
    """
    A set of NonEmptyStrings of size 1 or larger.
    """

    non_empty_strings: list[NonEmptyString | str]

    @validator("non_empty_strings")
    def check_non_empty_strings(
        cls, v: list[NonEmptyString | str]
    ) -> list[NonEmptyString]:
        if len(v) < 1:
            raise ValueError(
                "NonEmptyStringVector must contain at least one NonEmptyString"
            )
        validated_non_empty_strings = []
        for item in v:
            if isinstance(item, str):
                non_empty_string = NonEmptyString(value=item)
                validated_non_empty_strings.append(non_empty_string)
            elif not isinstance(item, NonEmptyString):
                raise ValueError(f"{item} is not a valid NonEmptyString")
            else:
                validated_non_empty_strings.append(item)
        return validated_non_empty_strings

    def __str__(self) -> str:
        return f"[{', '.join(map(str, self.non_empty_strings))}]"

    def __repr__(self) -> str:
        return (
            f"NonEmptyEmptyVector(non_empty_strings={self.non_empty_strings})"
        )
