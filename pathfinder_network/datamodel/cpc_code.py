from csv import DictReader
from pathlib import Path

from pydantic import BaseModel, validator


class CpcCode(BaseModel):
    """
    A CpCode represents a UN CPC Code version 2.1 value.
    """

    code: int
    descriptor: str = ""

    @validator("code")
    def code_must_be_valid(cls, v: int) -> int:
        codes_file_path = Path(__file__).parent / "data/cpc_codes_v21.csv"
        with open(codes_file_path, "r") as f:
            codes_reader = DictReader(f)
            for row in codes_reader:
                if int(row["CPC21code"]) == v:
                    return v
            raise ValueError(f"{v} is not a valid CPC code")

    @validator("descriptor", pre=False, always=True)
    def populate_descriptor(cls, v: str, values: dict[str, int | str]) -> str:
        if "code" in values:
            codes_file_path = Path(__file__).parent / "data/cpc_codes_v21.csv"
            with open(codes_file_path, "r") as f:
                codes_reader = DictReader(f)
                for row in codes_reader:
                    if int(row["CPC21code"]) == values["code"]:
                        return row["CPC21title"]
                raise ValueError(f"{v} is not a valid CPC code")
        else:
            return v

    def __str__(self) -> str:
        return str(self.code)

    def __repr__(self) -> str:
        return f"CpcCode(code={self.code}, descriptor={self.descriptor})"
