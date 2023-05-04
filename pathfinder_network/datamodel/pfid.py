from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class PfId(BaseModel):
    __root__: UUID = Field(default_factory=uuid4)

    @classmethod
    def from_str(cls, id_str: str) -> "PfId":
        return cls(__root__=UUID(id_str))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, PfId):
            return self.__root__ == other.__root__
        elif isinstance(other, str):
            return str(self.__root__) == other
        return False
