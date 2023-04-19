from pydantic import BaseModel


class String(BaseModel):
    """
    A regular UTF-8 String.
    """

    __root__: str

    def __str__(self) -> str:
        return self.__root__

    def __eq__(self, other: object) -> bool:
        if isinstance(other, String):
            return self.__root__ == other.__root__
        elif isinstance(other, str):
            return self.__root__ == other
        else:
            return NotImplemented
