import pytest

from pathfinder_network.datamodel.cpc_code import CpcCode


def test_valid_cpc_code():
    valid_code = 1103
    cpc = CpcCode(code=valid_code)
    assert cpc.code == valid_code
    assert cpc.descriptor == "Brown coal"


def test_invalid_cpc_code():
    invalid_code = 99999
    with pytest.raises(ValueError, match="99999 is not a valid CPC code") as exc:
        CpcCode(code=invalid_code)
    assert str(invalid_code) in str(exc.value)


def test_str_representation():
    code = 111
    cpc = CpcCode(code=code)
    assert str(cpc) == str(code)


def test_repr_representation():
    code = 13000
    descriptor = "Uranium and thorium ores and concentrates"
    cpc = CpcCode(code=code)
    assert repr(cpc) == f"CpcCode(code={code}, descriptor={descriptor})"
