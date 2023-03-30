from uuid import UUID

from pydantic import BaseModel


class PfId(BaseModel):
    id: UUID

    @classmethod
    def from_str(cls, id_str: str) -> "PfId":
        return cls(id=UUID(id_str))

    def __str__(self) -> str:
        return str(self.id)

    def __repr__(self) -> str:
        return f"PfId(id={str(self.id)})"
