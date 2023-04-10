from pydantic import BaseModel, validator

from pathfinder_network.datamodel.product_id import ProductId


class ProductIdSet(BaseModel):
    """
    A set of ProductIds of size 1 or larger.
    """

    product_ids: list[ProductId | str]

    @validator("product_ids")
    def check_product_ids(cls, v: list[ProductId | str]) -> list[ProductId]:
        if len(v) < 1:
            raise ValueError(
                "ProductIdSet must contain at least one ProductId"
            )
        validated_product_ids = []
        for item in v:
            if isinstance(item, str):
                product_id = ProductId(value=item)
                validated_product_ids.append(product_id)
            elif not isinstance(item, ProductId):
                raise ValueError(f"{item} is not a valid ProductId")
            else:
                validated_product_ids.append(item)
        return validated_product_ids

    def __str__(self) -> str:
        return f"[{', '.join(map(str, self.product_ids))}]"

    def __repr__(self) -> str:
        return f"ProductIdSet(product_ids={self.product_ids})"
