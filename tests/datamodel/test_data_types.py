import json

from pathfinder_network.datamodel.data_types import PfId


def test_pfid_is_uuid4():
    pfid: PfId = PfId()

    json_dict = json.dumps(dict(id=str(pfid.id)))

    assert pfid.json() == json_dict
