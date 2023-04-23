from pathfinder_network.datamodel.emission_factor_ds import EmissionFactorDS
from pathfinder_network.datamodel.non_empty_string import NonEmptyString


def test_valid_emission_factor_ds():
    name = NonEmptyString(__root__="ecoinvent")
    version = NonEmptyString(__root__="3.9.1")

    emission_factor_ds = EmissionFactorDS(name=name, version=version)

    assert emission_factor_ds.name == "ecoinvent"
    assert emission_factor_ds.version == "3.9.1"
