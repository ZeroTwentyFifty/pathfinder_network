from enum import Enum

from pydantic import BaseModel, Field

from pathfinder_network.datamodel.carbon_footprint import CarbonFootprint
from pathfinder_network.datamodel.company_id_set import CompanyIdSet
from pathfinder_network.datamodel.cpc_code import CpcCode
from pathfinder_network.datamodel.datetime import DateTime
from pathfinder_network.datamodel.pfid import PfId
from pathfinder_network.datamodel.product_id_set import ProductIdSet
from pathfinder_network.datamodel.string import String


class ProductFootprintStatus(str, Enum):
    """
    Status of a product footprint.

    Attributes:
        ACTIVE: The default status of a product footprint. A product footprint with
                status Active can be used by data recipients, e.g., for product
                footprint calculations.
        DEPRECATED: The product footprint is deprecated and should not be used for
                    e.g., product footprint calculations by data recipients.
    """

    ACTIVE = "Active"
    DEPRECATED = "Deprecated"


class ProductFootprint(BaseModel):
    """
    A ProductFootprint represents the carbon footprint of a product.

    Attributes:
        id (PfId): The product footprint identifier. See §4.29 Data Type: PfId for details.
        spec_version (String): The version of the ProductFootprint data specification with value 2.0.1-20230314.
                              Subsequent revisions will update this value according to Semantic Versioning 2.0.0.
        preceding_pfids (list[PfId] | None): If defined, MUST be a non-empty set of preceding product footprint
                                             identifiers without duplicates. See §4.29 Data Type: PfId and
                                             §5.2 Change Definition and Classification for details.
        version (int): The version of the ProductFootprint with a value in the inclusive range of 0..2^31-1.
        created (DateTime): The timestamp of the creation of the ProductFootprint.
        updated (DateTime | None): The timestamp of the ProductFootprint update. MUST NOT be included if an update
                                   has never been performed. The timestamp MUST be in UTC.
        status (ProductFootprintStatus): The status of the product footprint. See §5 Product Footprint Lifecycle
                                         for details.
        status_comment (String | None): A message explaining the reason for the current status.
                                       See 5 Product Footprint Lifecycle for details.
        validity_period_start (DateTime | None): The start of the validity period of the ProductFootprint.
                                               See §5 Product Footprint Lifecycle for details.
        validity_period_end (DateTime | None): The end (excluding) of the valid period of the ProductFootprint.
                                             See §5 Product Footprint Lifecycle for details.
        company_name (String): The name of the company that is the ProductFootprint Data Owner.
        company_ids (CompanyIdSet): The non-empty set of Uniform Resource Names (URN) identifying the
                                   ProductFootprint Data Owner. See CompanyIdSet for details.
        product_description (String): The free-form description of the product plus other information related to
                                     it, such as production technology or packaging.
        product_ids (ProductIdSet): The non-empty set of ProductIds. See §5 Product Footprint Lifecycle for details.
        product_category_cpc (CpcCode): A UN Product Classification Code (CPC) that the given product belongs to.
        product_name_company (String): The non-empty trade name of the product.
        comment (String): Additional information related to the product footprint. See §5 Product Footprint
                          Lifecycle for details.
        pcf (CarbonFootprint): The carbon footprint of the given product with a value conforming to the data type
                               CarbonFootprint.
        # TODO: extensions: Optional[List[DataModelExtension]].
    """

    id: PfId
    spec_version: String
    preceding_pfids: list[PfId] | None = None
    version: int = Field(..., ge=0, le=2**31 - 1)
    created: DateTime
    updated: DateTime | None = None
    status: ProductFootprintStatus
    status_comment: String | None = None
    validity_period_start: DateTime | None = None
    validity_period_end: DateTime | None = None
    company_name: String
    company_ids: CompanyIdSet
    product_description: String
    product_ids: ProductIdSet
    product_category_cpc: CpcCode
    product_name_company: String
    comment: String
    pcf: CarbonFootprint
    # TODO: extensions: Optional[List[DataModelExtension]]
