from pydantic import BaseModel, validator

from pathfinder_network.datamodel.company_id import CompanyId


class CompanyIdSet(BaseModel):
    """
    A set of CompanyIds of size 1 or larger.
    """

    company_ids: list[CompanyId | str]

    @validator("company_ids")
    def check_company_ids(cls, v: list[CompanyId | str]) -> list[CompanyId]:
        if len(v) < 1:
            raise ValueError(
                "CompanyIdSet must contain at least one CompanyId"
            )
        validated_company_ids = []
        for item in v:
            if isinstance(item, str):
                company_id = CompanyId(value=item)
                validated_company_ids.append(company_id)
            elif not isinstance(item, CompanyId):
                raise ValueError(f"{item} is not a valid CompanyId")
            else:
                validated_company_ids.append(item)
        return validated_company_ids

    def __str__(self) -> str:
        return f"[{', '.join(map(str, self.company_ids))}]"

    def __repr__(self) -> str:
        return f"CompanyIdSet(company_ids={self.company_ids})"
