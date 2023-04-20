from pydantic import BaseModel, validator

from pathfinder_network.datamodel.non_empty_string import NonEmptyString
from pathfinder_network.datamodel.non_empty_string_vector import (
    NonEmptyStringVector,
)
from pathfinder_network.datamodel.product_or_sector_specific_rule_operator import (  # NOQA: E501
    ProductOrSectorSpecificRuleOperator,
)

# TODO: LOOK INTO ORM_MODE IN PYDANTIC
# https://docs.pydantic.dev/usage/models/#automatically-excluded-attributes
#


class ProductOrSectorSpecificRule(BaseModel):
    operator: ProductOrSectorSpecificRuleOperator
    ruleNames: NonEmptyStringVector
    otherOperatorName: NonEmptyString | None = None

    @validator("otherOperatorName", pre=True, always=True)
    def check_operator(
        cls,
        v: NonEmptyString | None,
        values: dict[
            str,
            ProductOrSectorSpecificRuleOperator
            | NonEmptyStringVector
            | NonEmptyString
            | None,
        ],
    ) -> NonEmptyString | None:
        operator = values.get("operator")
        if (
            operator != ProductOrSectorSpecificRuleOperator.OTHER
            and v is not None
        ):
            raise ValueError(
                "otherOperatorName must be undefined when operator is not Other"  # NOQA: E501
            )
        if operator == ProductOrSectorSpecificRuleOperator.OTHER and v is None:
            raise ValueError(
                "otherOperatorName is required when operator is Other"
            )
        return v
