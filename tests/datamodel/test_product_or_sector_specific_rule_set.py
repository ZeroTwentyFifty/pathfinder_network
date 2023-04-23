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
from pathfinder_network.datamodel.product_or_sector_specific_rule_set import (
    ProductOrSectorSpecificRuleSet,
)


@pytest.fixture
def valid_poss_rule():
    operator = ProductOrSectorSpecificRuleOperator.PEF
    rules = NonEmptyStringVector(non_empty_strings=["rule1", "rule2"])

    poss_rule = ProductOrSectorSpecificRule(
        operator=operator, rule_names=rules
    )
    return poss_rule


def test_poss_rule_set_with_valid_rule(valid_poss_rule):
    poss_rule_set = ProductOrSectorSpecificRuleSet(rules=[valid_poss_rule])
    assert poss_rule_set.rules


def test_poss_rule_set_with_empty_list():
    with pytest.raises(
        ValueError,
        match="ProductOrSectorSpecificRuleSet must contain at least one ProductOrSectorSpecificRule",  # NOQA: E501
    ):
        ProductOrSectorSpecificRuleSet(rules=[])
