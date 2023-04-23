import pytest

from pathfinder_network.datamodel.product_or_sector_specific_rule_operator import (
    ProductOrSectorSpecificRuleOperator,
)


def test_valid_units():
    valid_rule_operators = ["PEF", "EPD International", "Other"]
    for rule_operator in valid_rule_operators:
        assert ProductOrSectorSpecificRuleOperator(rule_operator).value == rule_operator


def test_product_or_sector_specific_rule_operator():
    assert ProductOrSectorSpecificRuleOperator.PEF == "PEF"
    assert ProductOrSectorSpecificRuleOperator.EPD_INTERNATIONAL == "EPD International"
    assert ProductOrSectorSpecificRuleOperator.OTHER == "Other"


def test_invalid_unit():
    with pytest.raises(ValueError):
        ProductOrSectorSpecificRuleOperator("invalid unit")
