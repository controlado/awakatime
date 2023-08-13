import pytest

from awakatime import Awakatime


def test_base_url_is_correct(awakatime: Awakatime):
    assert awakatime.base_url == "https://wakatime.com"


@pytest.mark.asyncio
async def test_get_all_time_is_working(awakatime: Awakatime):
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


@pytest.mark.asyncio
async def test_get_projects_is_working(awakatime: Awakatime):
    data = await awakatime.get_projects()

    assert isinstance(data, list)
    assert all(isinstance(item, dict) for item in data)
