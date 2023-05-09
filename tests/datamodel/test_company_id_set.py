import pytest

from pathfinder_network.datamodel.company_id import CompanyId
from pathfinder_network.datamodel.company_id_set import CompanyIdSet


@pytest.fixture
def valid_company_id_string_list():
    ids = [
        "urn:pathfinder:company:customcode:buyer-assigned:4321",
        "urn:pathfinder:company:customcode:vendor-assigned:6789",
    ]
    return ids


@pytest.fixture
def valid_company_id_list():
    ids = [
        CompanyId(value="urn:pathfinder:company:customcode:buyer-assigned:4321"),
        CompanyId(value="urn:pathfinder:company:customcode:vendor-assigned:6789"),
    ]
    return ids


@pytest.fixture
def valid_company_id_set(valid_company_id_list):
    company_id_set = CompanyIdSet(company_ids=valid_company_id_list)
    return company_id_set


def test_company_id_set_with_valid_ids(valid_company_id_set, valid_company_id_list):
    assert valid_company_id_set.company_ids == valid_company_id_list


def test_company_id_set_with_valid_id_strings(valid_company_id_string_list):
    company_id_set = CompanyIdSet(company_ids=valid_company_id_string_list)
    assert (
        str(company_id_set) == f"[{', '.join(map(str, valid_company_id_string_list))}]"
    )


def test_company_id_set_comparison(valid_company_id_set, valid_company_id_list):
    company_id_set = CompanyIdSet(company_ids=valid_company_id_list)
    assert company_id_set == valid_company_id_set


def test_company_id_set_string_list_comparison(
    valid_company_id_list, valid_company_id_string_list
):
    company_id_set = CompanyIdSet(company_ids=valid_company_id_string_list)
    assert company_id_set == [
        "urn:pathfinder:company:customcode:buyer-assigned:4321",
        "urn:pathfinder:company:customcode:vendor-assigned:6789",
    ]


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
