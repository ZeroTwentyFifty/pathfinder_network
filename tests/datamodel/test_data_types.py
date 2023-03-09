import json
import uuid

from pathfinder_network.datamodel.data_types import PfId


def test_pfid_json_representation():
    pfid: PfId = PfId()

    json_dict = json.dumps(dict(id=str(pfid.id)))

    assert pfid.json() == json_dict


def test_pfid_is_uuid4():
    pfid: PfId = PfId()

    assert uuid.UUID(hex=str(pfid.id), version=4)
