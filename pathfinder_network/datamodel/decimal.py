from decimal import Decimal as PyDecimal
from typing import Union

from pydantic import BaseModel, validator


class Decimal(BaseModel):
    """
    A custom data type for a decimal number.

    Example values:

    10

    42.12

    -182.84

    JSON Representation:
    Each Decimal MUST be encoded as a JSON String.
    """

    value: Union[PyDecimal, float, int]

    @validator("value")
    def check_decimal(cls, v: Union[PyDecimal, float, int]) -> PyDecimal:
        if isinstance(v, PyDecimal):
            return v
        elif isinstance(v, (float, int)):
            return PyDecimal(str(v))
        else:
            raise ValueError("Decimal value must be a number")

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"Decimal(value={self.value})"
