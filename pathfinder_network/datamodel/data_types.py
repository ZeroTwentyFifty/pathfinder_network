import uuid

from pydantic import BaseModel


class PfId(BaseModel):
    id: uuid.UUID = uuid.uuid4()
