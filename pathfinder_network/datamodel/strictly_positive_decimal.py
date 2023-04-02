from decimal import Decimal

from pydantic import BaseModel, validator


class StrictlyPositiveDecimal(BaseModel):
    """
    A positive, non-zero Decimal.

    Example values:
    - 0.123
    - 1000
    - 42.102340
    """

    value: Decimal

    @validator("value")
    def check_positive(cls, v: Decimal) -> Decimal:
        if v <= 0:
            raise ValueError("Value must be a positive, non-zero Decimal")
        return v

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"StrictlyPositiveDecimal(value={self.value})"
