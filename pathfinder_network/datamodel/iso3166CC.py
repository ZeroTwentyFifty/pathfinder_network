import pycountry
from pydantic import BaseModel, validator


class ISO3166CC(BaseModel):
    """
    An ISO 3166-2 alpha-2 country code.

    Example value for tue alpha-2 country code of the United States:
        US
    """

    code: str

    @validator("code")
    def check_code(cls, v: str) -> str:
        country = pycountry.countries.get(alpha_2=v)
        if country is None:
            raise ValueError(f"Invalid ISO 3166-2 alpha-2 country code: {v}")
        else:
            return country.alpha_2

    def __str__(self) -> str:
        return self.code

    def __repr__(self) -> str:
        return f"ISO3166CC(code={self.code})"
