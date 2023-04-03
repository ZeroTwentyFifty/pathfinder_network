from decimal import Decimal

from pydantic import BaseModel, validator


class Percent(BaseModel):
    """
    A Decimal number in the range of and including 0 and 100.

    Example values:
    - 100
    - 23.0
    - 7.183924
    - 0.0
    """

    value: Decimal

    @validator("value")
    def check_range(cls, v: Decimal) -> Decimal:
        if not (0 <= v <= 100):
            raise ValueError("Value must be in the range [0, 100]")
        return v

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"Percent(value={self.value})"
