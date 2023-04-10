from pathfinder_network.datamodel.urn import URN


class ProductId(URN):
    """
    A URN conforming to the ProductId syntax.

    TODO: Implement the additional functionality to support SHOULD behaviour
        4.21.1. Custom Product Ids (Product Codes)
        4.21.2. ProductId based on CAS Registry Numbers
        4.21.3. ProductId based on IUPAC InChi Code
    """

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"ProductId(value='{self.value}')"
