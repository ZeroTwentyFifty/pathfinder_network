import pytest

from pathfinder_network.datamodel.company_id import CompanyId


def test_valid_company_id():
    p = CompanyId(value="urn:pathfinder:company:customcode:buyer-assigned:4321")
    assert str(p) == "urn:pathfinder:company:customcode:buyer-assigned:4321"

    p = CompanyId(value="urn:pathfinder:company:customcode:vendor-assigned:6789")
    assert str(p) == "urn:pathfinder:company:customcode:vendor-assigned:6789"


def test_invalid_company_id():
    with pytest.raises(ValueError, match="Value must be a valid URN"):
        CompanyId(value="definitely-gonna-fail")
