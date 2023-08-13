from os import environ

import pytest

from awakatime import Awakatime


@pytest.fixture
async def awakatime():
    wakatime_token = environ["WAKATIME_API_KEY"]
    async with Awakatime(wakatime_token) as awakatime:
        yield awakatime
