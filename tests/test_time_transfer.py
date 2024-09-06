from datetime import datetime

import pytest

from utils.time_transfer import TimeTransfer


@pytest.mark.parametrize(
    "input_time, format, expected_time",
    [
        ("2024-09-04", "%Y-%m-%d", datetime(2024, 9, 4)),
        ("2024-09-04 12:30:45", "%Y-%m-%d %H:%M:%S", datetime(2024, 9, 4, 12, 30, 45)),
        ("2024-09-04 12:30", "%Y-%m-%d %H:%M", datetime(2024, 9, 4, 12, 30)),
    ],
)
def test_time_transfer_success(input_time, format, expected_time):
    assert TimeTransfer.str_to_datetime(input_time, format) == expected_time


@pytest.mark.parametrize(
    "input_time, format, expected_time",
    [
        ("2024-09-04", "%Y-%m-%d %H", datetime(2024, 9, 4)),
        ("2024-09-04 12:30:45", "%Y-%m-%d", datetime(2024, 9, 4, 12, 30, 45)),
    ],
)
def test_time_transfer_fail(input_time, format, expected_time):
    with pytest.raises(ValueError):
        TimeTransfer.str_to_datetime(input_time, format)


@pytest.mark.parametrize(
    "input_time, format, expected_time",
    [
        (datetime(2024, 9, 6, 10, 28), "%Y-%m-%d %H:%M", "2024-09-06 10:28"),
        (datetime(2024, 9, 6, 10, 28, 30), "%Y-%m-%d %H:%M:%S", "2024-09-06 10:28:30"),
        (datetime(2024, 9, 6), "%Y-%m-%d", "2024-09-06"),
    ],
)
def test_datetime_to_str_success(input_time, format, expected_time):
    assert TimeTransfer.datetime_to_str(input_time, format) == expected_time
