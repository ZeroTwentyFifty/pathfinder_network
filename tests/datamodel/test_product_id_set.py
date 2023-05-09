import pytest

from pathfinder_network.datamodel.product_id import ProductId
from pathfinder_network.datamodel.product_id_set import ProductIdSet


@pytest.fixture
def valid_product_id_string_list():
    ids = [
        "urn:pathfinder:product:customcode:buyer-assigned:4321",
        "urn:pathfinder:product:customcode:vendor-assigned:6789",
    ]
    return ids


@pytest.fixture
def valid_product_id_list():
    ids = [
        ProductId(value="urn:foo:params:pid:product:customcode:buyer-assigned:foo-bar"),
        ProductId(value="urn:foo:params:pid:product:id:cas:1234-56-8"),
        ProductId(
            value="urn:foo:params:pid:product:id:iupac-inchi:InChI=1S/C6H12O6/c7-1-2-3(8)4(9)5(10)6(11)12-2/h2-11H,1H2/t2-,3-,4+,5-,6?/m1/s1"
        ),
    ]
    return ids


@pytest.fixture
def valid_product_id_set(valid_product_id_list):
    product_id_set = ProductIdSet(product_ids=valid_product_id_list)
    return product_id_set


def test_product_id_set_with_valid_ids(valid_product_id_set, valid_product_id_list):
    assert valid_product_id_set.product_ids == valid_product_id_list


def test_product_id_set_with_valid_id_strings():
    ids = [
        "urn:foo:params:pid:product:customcode:buyer-assigned:foo-bar",
        "urn:foo:params:pid:product:id:cas:1234-56-8",
        "urn:foo:params:pid:product:id:iupac-inchi:InChI=1S/C6H12O6/c7-1-2-3(8)4(9)5(10)6(11)12-2/h2-11H,1H2/t2-,3-,4+,5-,6?/m1/s1",
    ]
    product_id_set = ProductIdSet(product_ids=ids)
    assert str(product_id_set) == f"[{', '.join(map(str, ids))}]"


def test_product_id_set_comparison(valid_product_id_set, valid_product_id_list):
    product_id_set = ProductIdSet(product_ids=valid_product_id_list)
    assert product_id_set == valid_product_id_set


def test_product_id_set_string_list_comparison(
    valid_product_id_list, valid_product_id_string_list
):
    product_id_set = ProductIdSet(product_ids=valid_product_id_string_list)
    assert product_id_set == [
        "urn:pathfinder:product:customcode:buyer-assigned:4321",
        "urn:pathfinder:product:customcode:vendor-assigned:6789",
    ]


def test_product_id_set_with_empty_list():
    with pytest.raises(
        ValueError, match="ProductIdSet must contain at least one ProductId"
    ):
        ProductIdSet(product_ids=[])


def test_product_id_set_with_invalid_id():
    ids = [
        ProductId(value="urn:foo:params:pid:product:customcode:buyer-assigned:foo-bar"),
        ProductId(value="urn:foo:params:pid:product:id:cas:1234-56-8"),
        "invalid-urn",
    ]
    with pytest.raises(ValueError, match="Value must be a valid URN"):
        ProductIdSet(product_ids=ids)
