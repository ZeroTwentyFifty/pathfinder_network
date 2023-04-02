from datetime import datetime, timezone

from pydantic import BaseModel, validator


class DateTime(BaseModel):
    """
    A date and time string conforming to ISO 8601 in UTC timezone.

    Example value for beginning of March, the year 2020, UTC:
        2020-03-01T00:00:00Z
    """

    value: datetime

    @validator("value")
    def check_datetime(cls, v: datetime) -> datetime:
        if v.tzinfo != timezone.utc:
            raise ValueError("DateTime must be in UTC timezone")
        else:
            return v

    def __str__(self) -> str:
        return self.value.isoformat()

    def __repr__(self) -> str:
        return f"DateTime(value='{self.value.isoformat()}')"
