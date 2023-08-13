import pytest

from awakatime import Awakatime


@pytest.mark.asyncio
async def test_get_all_time(awakatime: Awakatime):
    correct_keys = [
        "decimal",
        "digital",
        "is_up_to_date",
        "percent_calculated",
        "range",
        "text",
        "timeout",
        "total_seconds",
    ]
    data = await awakatime.get_all_time()

    assert isinstance(data, dict)
    assert all(key in data for key in correct_keys)
