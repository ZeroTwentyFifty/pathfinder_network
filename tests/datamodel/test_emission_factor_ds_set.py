import pytest

from pathfinder_network.datamodel.emission_factor_ds import EmissionFactorDS
from pathfinder_network.datamodel.emission_factor_ds_set import EmissionFactorDSSet
from pathfinder_network.datamodel.non_empty_string import NonEmptyString


@pytest.fixture
def valid_emission_factor_ds():
    name = NonEmptyString(__root__="ecoinvent")
    version = NonEmptyString(__root__="3.9.1")

    dataset = EmissionFactorDS(name=name, version=version)

    return dataset


def test_emission_factor_ds_set_with_valid_standard(valid_emission_factor_ds):
    emission_factor_ds_set = EmissionFactorDSSet(datasets=[valid_emission_factor_ds])
    assert emission_factor_ds_set.datasets


def test_emission_factor_ds_set_with_empty_list():
    with pytest.raises(
        ValueError,
        match="EmissionFactorDSSet must contain at least one EmissionFactorDS",
    ):
        EmissionFactorDSSet(datasets=[])
