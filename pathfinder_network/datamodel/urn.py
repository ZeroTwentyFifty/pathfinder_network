from pydantic import BaseModel, validator
from urnparse import URN8141, InvalidURNFormatError


class URN(BaseModel):
    """
    A String conforming to the URN syntax.
    """

    value: str

    @validator("value")
    def check_valid_urn(cls, v: str) -> str:
        try:
            URN8141.from_string(v)
        except InvalidURNFormatError:
            raise ValueError("Value must be a valid URN")
        return v

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"URN(value='{self.value}')"
