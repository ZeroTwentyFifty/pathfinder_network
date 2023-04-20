import pytest

from pathfinder_network.datamodel.non_empty_string_vector import (
    NonEmptyStringVector,
)
from pathfinder_network.datamodel.product_or_sector_specific_rule import (
    ProductOrSectorSpecificRule,
)
from pathfinder_network.datamodel.product_or_sector_specific_rule_operator import (  # NOQA: E501
    ProductOrSectorSpecificRuleOperator,
)


def test_valid_product_or_sector_specific_rule():
    # Valid input
    operator = ProductOrSectorSpecificRuleOperator.PEF
    rule_names = NonEmptyStringVector(non_empty_strings=["rule 1", "rule 2"])

    # Creating the ProductOrSectorSpecificRule object
    product_or_sector_specific_rule = ProductOrSectorSpecificRule(
        operator=operator, ruleNames=rule_names
    )

    for rule in rule_names.non_empty_strings:
        assert rule.__root__.startswith("rule")

    # Asserting the output
    assert product_or_sector_specific_rule.operator == "PEF"
    assert product_or_sector_specific_rule.otherOperatorName is None
    assert (
        product_or_sector_specific_rule.ruleNames.non_empty_strings[1]
        == "rule 2"
    )


def test_invalid_product_or_sector_specific_rule_other_operator_name_undefined():  # NOQA: E501
    # Invalid input: otherOperatorName must be undefined when operator is not Other  # NOQA: E501
    operator = ProductOrSectorSpecificRuleOperator.PEF
    rule_names = ["rule 1", "rule 2"]
    other_operator_name = "test"

    # Checking for expected ValueError
    with pytest.raises(
        ValueError,
        match="otherOperatorName must be undefined when operator is not Other",
    ):
        ProductOrSectorSpecificRule(
            operator=operator,
            ruleNames=rule_names,
            otherOperatorName=other_operator_name,
        )


def test_invalid_product_or_sector_specific_rule_other_operator_name_defined():
    # Invalid input: otherOperatorName is required when operator is Other
    operator = ProductOrSectorSpecificRuleOperator.OTHER
    rule_names = NonEmptyStringVector(non_empty_strings=["rule 1"])
    other_operator_name = None

    # Checking for expected ValueError
    with pytest.raises(
        ValueError,
        match="otherOperatorName is required when operator is Other",
    ):
        ProductOrSectorSpecificRule(
            operator=operator,
            ruleNames=rule_names,
            otherOperatorName=other_operator_name,
        )
