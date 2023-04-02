from datetime import datetime, timezone

import pytest

from pathfinder_network.datamodel.datetime import DateTime


def test_valid_datetime():
    dt = DateTime(value="2022-04-01T12:00:00Z")
    assert str(dt) == "2022-04-01T12:00:00+00:00"
    assert repr(dt) == "DateTime(value='2022-04-01T12:00:00+00:00')"
    assert dt.value == datetime(2022, 4, 1, 12, 0, 0, tzinfo=timezone.utc)


def test_invalid_datetime_format():
    # Invalid format (should be in ISO 8601 format)
    with pytest.raises(ValueError):
        DateTime(value="2020-03-01 00:00:00")

    # Invalid format (should not have milliseconds)
    with pytest.raises(ValueError):
        DateTime(value="2022-04-05T13:30:00.123")

    # Invalid format (should use "-" as delimiter instead of "/")
    with pytest.raises(ValueError):
        DateTime(value="2022/04/05T13:30:00Z")


def test_non_utc_timezone():
    with pytest.raises(ValueError):
        DateTime(value="2022-04-01T12:00:00-08:00")


def test_extra_timezones():
    # invalid datetime string with incorrect timezone offset format
    dt_str = "2022-04-01T12:30:00+2:00"
    with pytest.raises(ValueError):
        DateTime(value=dt_str)

    # invalid datetime string with incorrect timezone abbreviation
    dt_str = "2022-04-01T12:30:00EST"
    with pytest.raises(ValueError):
        DateTime(value=dt_str)
