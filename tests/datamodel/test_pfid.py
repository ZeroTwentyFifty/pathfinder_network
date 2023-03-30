import uuid

import pytest
from pydantic import ValidationError

from pathfinder_network.datamodel.pfid import PfId


def test_valid_pf_id():
    # Test that a valid PfId is created with the correct value
    uuid_str = "142b32a7-7c3c-4a6e-baed-d11a14e49eb2"
    pf_id = PfId(id=uuid_str)
    assert pf_id.id == uuid.UUID(uuid_str)
    assert str(pf_id) == uuid_str


def test_invalid_pf_id():
    # Test that an invalid PfId raises a ValidationError
    invalid_uuid_str = "invalid_uuid_string"
    with pytest.raises(ValidationError):
        PfId(id=invalid_uuid_str)
