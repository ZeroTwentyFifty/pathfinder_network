import pytest

from pathfinder_network.datamodel.company_id import CompanyId
from pathfinder_network.datamodel.company_id_set import CompanyIdSet


def test_company_id_set_with_valid_ids():
    ids = [
        CompanyId(value="urn:pathfinder:company:customcode:buyer-assigned:4321"),
        CompanyId(value="urn:pathfinder:company:customcode:vendor-assigned:6789"),
    ]
    company_id_set = CompanyIdSet(company_ids=ids)
    assert company_id_set.company_ids == ids


def test_company_id_set_with_valid_id_strings():
    ids = [
        "urn:pathfinder:company:customcode:buyer-assigned:4321",
        "urn:pathfinder:company:customcode:vendor-assigned:6789",
    ]
    company_id_set = CompanyIdSet(company_ids=ids)
    assert str(company_id_set) == f"[{', '.join(map(str, ids))}]"


def test_company_id_set_with_empty_list():
    with pytest.raises(
        ValueError, match="CompanyIdSet must contain at least one CompanyId"
    ):
        CompanyIdSet(company_ids=[])


def test_company_id_set_with_invalid_id():
    ids = [
        CompanyId(value="urn:pathfinder:company:customcode:buyer-assigned:4321"),
        CompanyId(value="urn:pathfinder:company:customcode:vendor-assigned:6789"),
        "invalid-urn",
    ]
    with pytest.raises(ValueError, match="Value must be a valid URN"):
        CompanyIdSet(company_ids=ids)
