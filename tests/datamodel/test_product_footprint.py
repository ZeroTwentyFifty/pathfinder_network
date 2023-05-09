import pytest
from pydantic import ValidationError

from pathfinder_network.datamodel.carbon_footprint import CarbonFootprint
from pathfinder_network.datamodel.company_id_set import CompanyIdSet
from pathfinder_network.datamodel.cpc_code import CpcCode
from pathfinder_network.datamodel.cross_sectoral_standard import CrossSectoralStandard
from pathfinder_network.datamodel.cross_sectoral_standard_set import (
    CrossSectoralStandardSet,
)
from pathfinder_network.datamodel.datetime import DateTime
from pathfinder_network.datamodel.decimal import Decimal
from pathfinder_network.datamodel.declared_unit import DeclaredUnit
from pathfinder_network.datamodel.percent import Percent
from pathfinder_network.datamodel.pfid import PfId
from pathfinder_network.datamodel.product_footprint import (
    ProductFootprint,
    ProductFootprintStatus,
)
from pathfinder_network.datamodel.product_id_set import ProductIdSet
from pathfinder_network.datamodel.string import String


@pytest.fixture
def valid_start_datetime():
    return DateTime(value="2023-04-01T12:00:00Z")


@pytest.fixture
def valid_end_datetime():
    return DateTime(value="2024-04-01T12:00:00Z")


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ("Active", ProductFootprintStatus.ACTIVE),
        ("Deprecated", ProductFootprintStatus.DEPRECATED),
    ],
)
def test_product_footprint_status_enum(input_value, expected_output):
    assert ProductFootprintStatus(input_value) == expected_output


def test_product_footprint_status_enum_invalid_value():
    with pytest.raises(ValueError):
        ProductFootprintStatus("invalid unit")


def test_product_footprint_all_mandatory_fields(
    valid_start_datetime, valid_end_datetime, valid_carbon_footprint
):
    company_ids = CompanyIdSet(company_ids=["urn:epc:id:sgln:0614141.00002.0"])
    product_ids = ProductIdSet(product_ids=["urn:epc:id:gtin:0614141.011111.0"])
    cpc_code = CpcCode(code=22222)

    uuid_str = "142b32a7-7c3c-4a6e-baed-d11a14e49eb2"

    product_footprint = ProductFootprint(
        id=PfId.from_str(uuid_str),
        spec_version=String(__root__="2.0.1-20230314"),
        version=1,
        created=valid_start_datetime,
        status=ProductFootprintStatus.ACTIVE,
        company_name=String(__root__="Example Company"),
        company_ids=company_ids,
        product_description=String(__root__="Example product description"),
        product_ids=product_ids,
        product_category_cpc=cpc_code,
        product_name_company=String(__root__="Example Product Name"),
        comment=String(__root__="Example comment"),
        pcf=valid_carbon_footprint,
    )

    assert product_footprint.id == uuid_str
    assert product_footprint.spec_version == "2.0.1-20230314"
    assert product_footprint.version == 1
    assert product_footprint.created == "2023-04-01T12:00:00+00:00"
    assert product_footprint.status == "Active"
    assert product_footprint.company_name == "Example Company"
    assert product_footprint.company_ids == ["urn:epc:id:sgln:0614141.00002.0"]
    assert product_footprint.product_description == "Example product description"
    assert product_footprint.product_ids == ["urn:epc:id:gtin:0614141.011111.0"]
    assert product_footprint.product_category_cpc == 22222
    assert product_footprint.product_name_company == "Example Product Name"
    assert product_footprint.comment == "Example comment"


def test_product_footprint_invalid_attributes(valid_carbon_footprint):
    """Test that creating a ProductFootprint with invalid attributes raises a ValidationError"""
    company_ids = CompanyIdSet(company_ids=["urn:epc:id:sgln:0614141.00002.0"])
    product_ids = ProductIdSet(product_ids=["urn:epc:id:gtin:0614141.011111.0"])
    cpc_code = CpcCode(code=22222)

    with pytest.raises(ValidationError):
        ProductFootprint(
            id=PfId(),
            spec_version=String(__root__="2.0.1-20230314"),
            version=-1,
            created=DateTime(value="2023-04-01T12:00:00Z"),
            status=ProductFootprintStatus.ACTIVE,
            company_name=String(__root__="Example Company"),
            company_ids=company_ids,
            product_description=String(__root__="Example product description"),
            product_ids=product_ids,
            product_category_cpc=cpc_code,
            product_name_company=String(__root__="Example Product Name"),
            comment=String(__root__="Example comment"),
            pcf=valid_carbon_footprint,
        )
