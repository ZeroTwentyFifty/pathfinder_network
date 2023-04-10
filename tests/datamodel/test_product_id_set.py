import pytest

from pathfinder_network.datamodel.product_id import ProductId
from pathfinder_network.datamodel.product_id_set import ProductIdSet


def test_product_id_set_with_valid_ids():
    ids = [
        ProductId(
            value="urn:foo:params:pid:product:customcode:buyer-assigned:foo-bar"  # noqa: E501
        ),
        ProductId(value="urn:foo:params:pid:product:id:cas:1234-56-8"),
        ProductId(
            value="urn:foo:params:pid:product:id:iupac-inchi:InChI=1S/C6H12O6/c7-1-2-3(8)4(9)5(10)6(11)12-2/h2-11H,1H2/t2-,3-,4+,5-,6?/m1/s1"  # noqa: E501
        ),  # noqa: E501
    ]
    product_id_set = ProductIdSet(product_ids=ids)
    assert product_id_set.product_ids == ids


def test_product_id_set_with_valid_id_strings():
    ids = [
        "urn:foo:params:pid:product:customcode:buyer-assigned:foo-bar",
        "urn:foo:params:pid:product:id:cas:1234-56-8",
        "urn:foo:params:pid:product:id:iupac-inchi:InChI=1S/C6H12O6/c7-1-2-3(8)4(9)5(10)6(11)12-2/h2-11H,1H2/t2-,3-,4+,5-,6?/m1/s1",  # noqa: E501
    ]
    product_id_set = ProductIdSet(product_ids=ids)
    assert str(product_id_set) == f"[{', '.join(map(str, ids))}]"


def test_product_id_set_with_empty_list():
    with pytest.raises(
        ValueError, match="ProductIdSet must contain at least one ProductId"
    ):
        ProductIdSet(product_ids=[])


def test_product_id_set_with_invalid_id():
    ids = [
        ProductId(
            value="urn:foo:params:pid:product:customcode:buyer-assigned:foo-bar"  # noqa: E501
        ),
        ProductId(value="urn:foo:params:pid:product:id:cas:1234-56-8"),
        "invalid-urn",
    ]
    with pytest.raises(ValueError, match="Value must be a valid URN"):
        ProductIdSet(product_ids=ids)
