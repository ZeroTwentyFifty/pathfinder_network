from pathfinder_network.datamodel.urn import URN


class CompanyId(URN):
    """
    A URN conforming to the CompanyId syntax.

    TODO: Implement the additional functionality to support SHOULD behaviour
        4.19.1. Custom Company Ids (Company Codes)
    """

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"CompanyId(value='{self.value}')"
