import pytest

from pathfinder_network.datamodel.assurance import (
    AssuranceBoundary,
    AssuranceCoverage,
    AssuranceLevel,
)


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ("corporate level", AssuranceCoverage.corporate_level),
        ("product line", AssuranceCoverage.product_line),
        ("PCF system", AssuranceCoverage.pcf_system),
        ("product level", AssuranceCoverage.product_level),
    ],
)
def test_coverage_enum(input_value, expected_output):
    assert AssuranceCoverage(input_value) == expected_output


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ("limited", AssuranceLevel.limited),
        ("reasonable", AssuranceLevel.reasonable),
    ],
)
def test_level_enum(input_value, expected_output):
    assert AssuranceLevel(input_value) == expected_output


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ("Gate-to-Gate", AssuranceBoundary.gate_to_gate),
        ("Cradle-to-Gate", AssuranceBoundary.cradle_to_gate),
    ],
)
def test_boundary_enum(input_value, expected_output):
    assert AssuranceBoundary(input_value) == expected_output
