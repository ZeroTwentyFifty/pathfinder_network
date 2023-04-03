from pydantic import BaseModel


class String(BaseModel):
    """
    A regular UTF-8 String.
    """

    value: str

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"String(value={self.value})"
