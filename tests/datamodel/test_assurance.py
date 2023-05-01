import pytest

from pathfinder_network.datamodel.assurance import (
    Assurance,
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


def test_valid_assurance():
    assurance = Assurance(assurance=True)

    assert assurance.assurance is True


def test_valid_assurance_with_enums():
    assurance = Assurance(
        assurance=True,
        coverage=AssuranceCoverage.corporate_level,
        level=AssuranceLevel.limited,
        boundary=AssuranceBoundary.gate_to_gate,
    )

    assert assurance.assurance is True
    assert assurance.coverage == "corporate level"
    assert assurance.level == "limited"
    assert assurance.boundary == "Gate-to-Gate"
