from uuid import UUID

import pytest

from pathfinder_network.datamodel.pfid import PfId


def test_valid_pf_id():
    # Test that a valid PfId is created with the correct value
    pf_id = PfId()
    assert isinstance(pf_id.__root__, UUID)


def test_valid_pfid_from_str():
    uuid_str = "142b32a7-7c3c-4a6e-baed-d11a14e49eb2"
    pfid = PfId.from_str(uuid_str)

    assert isinstance(pfid.__root__, UUID)


def test_valid_pfid_comparison():
    uuid_str = "142b32a7-7c3c-4a6e-baed-d11a14e49eb2"
    pfid1 = PfId.from_str(uuid_str)
    pfid2 = PfId.from_str(uuid_str)

    assert pfid1 == uuid_str
    assert pfid1 == pfid2


def test_invalid_pfid_from_str():
    invalid_uuid_str = "obviously invalid"
    with pytest.raises(ValueError):
        PfId.from_str(invalid_uuid_str)
