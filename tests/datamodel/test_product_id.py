import pytest

from pathfinder_network.datamodel.product_id import ProductId


def test_valid_product_id():
    p = ProductId(
        value="urn:pathfinder:product:customcode:buyer-assigned:1234"
    )
    assert str(p) == "urn:pathfinder:product:customcode:buyer-assigned:1234"

    p = ProductId(
        value="urn:pathfinder:product:customcode:vendor-assigned:8765"
    )
    assert str(p) == "urn:pathfinder:product:customcode:vendor-assigned:8765"

    p = ProductId(value="urn:pathfinder:product:id:cas:64-17-5")
    assert str(p) == "urn:pathfinder:product:id:cas:64-17-5"

    p = ProductId(
        value="urn:pathfinder:product:id:iupac-inchi:1S%2FC9H8O4%2Fc1-6%2810%2913-8-5-3-2-4-7%288%299%2811%2912%2Fh2-5H%2C1H3%2C%28H%2C11%2C12%29"  # noqa: E501
    )
    assert (
        str(p)
        == "urn:pathfinder:product:id:iupac-inchi:1S%2FC9H8O4%2Fc1-6%2810%2913-8-5-3-2-4-7%288%299%2811%2912%2Fh2-5H%2C1H3%2C%28H%2C11%2C12%29"  # noqa: E501
    )


@pytest.mark.xfail(
    reason="Will fail until https://github.com/JohnVonNeumann/pathfinder_network/issues/1 completed."  # noqa: E501
)
def test_invalid_product_id():
    with pytest.raises(ValueError, match="Value must be a valid URN"):
        ProductId(
            value="urn:pathfinder:product:customcode:buyer-assigned:1234"
        )

    with pytest.raises(ValueError, match="Invalid ProductId"):
        ProductId(value="urn:pathfinder:foo:customcode:vendor-assigned:8765")

    with pytest.raises(
        ValueError, match="string too long (maximum 50 characters)"
    ):
        ProductId(
            value="urn:pathfinder:product:customcode:vendor-assigned:"
            + "x" * 51
        )

    with pytest.raises(ValueError, match="Invalid ProductId"):
        ProductId(value="urn:pathfinder:product:id:foo:64-17-5")

    with pytest.raises(ValueError, match="Value must be a valid URN"):
        ProductId(value="urn:pathfinder:product:id:iupac-inchi:")

    with pytest.raises(
        ValueError, match="string too long (maximum 10000 characters)"
    ):
        ProductId(value="urn:pathfinder:product:id:iupac-inchi:" + "x" * 10001)
