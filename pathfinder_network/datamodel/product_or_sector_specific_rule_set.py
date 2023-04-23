from pydantic import BaseModel, validator

from pathfinder_network.datamodel.product_or_sector_specific_rule import (
    ProductOrSectorSpecificRule,
)


class ProductOrSectorSpecificRuleSet(BaseModel):
    """
    A set of ProductOrSectorSpecificRules of size 1 or larger.

    Attributes:
        rules (list[ProductOrSectorSpecificRule]): A list of ProductOrSectorSpecificRule objects.

    Raises:
        ValueError: If the list of rules is empty.
    """

    rules: list[ProductOrSectorSpecificRule]

    @validator("rules")
    def check_rules(
        cls, v: list[ProductOrSectorSpecificRule]
    ) -> list[ProductOrSectorSpecificRule]:
        if len(v) < 1:
            raise ValueError(
                "ProductOrSectorSpecificRuleSet must contain at least one ProductOrSectorSpecificRule"
            )
        return v
