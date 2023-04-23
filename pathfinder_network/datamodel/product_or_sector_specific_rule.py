from pydantic import BaseModel, validator

from pathfinder_network.datamodel.non_empty_string import NonEmptyString
from pathfinder_network.datamodel.non_empty_string_vector import NonEmptyStringVector
from pathfinder_network.datamodel.product_or_sector_specific_rule_operator import (
    ProductOrSectorSpecificRuleOperator,
)

# TODO: LOOK INTO ORM_MODE IN PYDANTIC
# https://docs.pydantic.dev/usage/models/#automatically-excluded-attributes
#


class ProductOrSectorSpecificRule(BaseModel):
    """
    A rule specifying conditions for filtering data based on the product or sector.

    Attributes:
        operator (ProductOrSectorSpecificRuleOperator): An operator representing the type of the rule.
        rule_names (NonEmptyStringVector): A set of non-empty string values representing the names of the rules.
        other_operator_name (Union[NonEmptyString, None]): A non-empty string representing the name of the rule, if the
                                                           operator is 'OTHER'.

    Raises:
        ValueError: If other_operator_name is defined but the operator is not 'OTHER', or if other_operator_name is not
                    defined but the operator is 'OTHER'.
    """

    operator: ProductOrSectorSpecificRuleOperator
    rule_names: NonEmptyStringVector
    other_operator_name: NonEmptyString | None = None

    @validator("other_operator_name", pre=True, always=True)
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
        if operator != ProductOrSectorSpecificRuleOperator.OTHER and v is not None:
            raise ValueError(
                "other_operator_name must be undefined when operator is not Other"
            )
        if operator == ProductOrSectorSpecificRuleOperator.OTHER and v is None:
            raise ValueError("other_operator_name is required when operator is Other")
        return v
