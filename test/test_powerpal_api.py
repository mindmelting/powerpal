import pytest
from aiohttp import ClientSession, ServerTimeoutError

from aioresponses import aioresponses
from test.example_responses import (
    EXAMPLE_RESPONSE,
    EXAMPLE_TIME_SERIES_RESPONSE,
    EXAMPLE_TIME_SERIES_END_ONLY_RESPONSE,
    EXAMPLE_TIME_SERIES_START_END_RESPONSE,
    EXAMPLE_TIME_SERIES_SAMPLE_60_RESPONSE,
    EXAMPLE_TIME_SERIES_START_ONLY_RESPONSE,
    EXAMPLE_TIME_SERIES_START_SAMPLE_60_RESPONSE,
    EXAMPLE_TIME_SERIES_START_END_SAMPLE_60_RESPONSE,
)

from mindmelting.powerpal import Powerpal
from mindmelting.powerpal.exceptions import (
    PowerpalException,
    PowerpalAuthorizationException,
    PowerpalAuthenticationException
)


BASE_URL = "https://readings.powerpal.net/api/v1"
EXAMPLE_DEVICE_ID = "12345"
EXAMPLE_AUTH_STR = "abcd"


async def test_success():
    with aioresponses() as m:
        m.get(
            url=f'{BASE_URL}/device/{EXAMPLE_DEVICE_ID}',
            status=200,
            payload=EXAMPLE_RESPONSE
        )

        async with ClientSession() as session:
            powerpal = Powerpal(session, EXAMPLE_AUTH_STR, EXAMPLE_DEVICE_ID)
            data = await powerpal.get_data()

        assert data == EXAMPLE_RESPONSE


async def test_time_series_success():
    with aioresponses() as m:
        m.get(
            url=f'{BASE_URL}/meter_reading/{EXAMPLE_DEVICE_ID}',
            status=200,
            payload=EXAMPLE_TIME_SERIES_RESPONSE
        )

        async with ClientSession() as session:
            powerpal = Powerpal(session, EXAMPLE_AUTH_STR, EXAMPLE_DEVICE_ID)
            data = await powerpal.get_time_series_data()

        assert data == EXAMPLE_TIME_SERIES_RESPONSE


async def test_time_series_start_only_success():
    with aioresponses() as m:
        m.get(
            url=f'{BASE_URL}/meter_reading/{EXAMPLE_DEVICE_ID}?'
            f'start=1706321820',
            status=200,
            payload=EXAMPLE_TIME_SERIES_START_ONLY_RESPONSE
        )

        async with ClientSession() as session:
            powerpal = Powerpal(session, EXAMPLE_AUTH_STR, EXAMPLE_DEVICE_ID)
            data = await powerpal.get_time_series_data(start=1706321820)

        assert data == EXAMPLE_TIME_SERIES_START_ONLY_RESPONSE


async def test_time_series_end_only_success():
    with aioresponses() as m:
        m.get(
            url=f'{BASE_URL}/meter_reading/{EXAMPLE_DEVICE_ID}?'
            f'end=1706321880',
            status=200,
            payload=EXAMPLE_TIME_SERIES_END_ONLY_RESPONSE
        )

        async with ClientSession() as session:
            powerpal = Powerpal(session, EXAMPLE_AUTH_STR, EXAMPLE_DEVICE_ID)
            data = await powerpal.get_time_series_data(end=1706321880)

        assert data == EXAMPLE_TIME_SERIES_END_ONLY_RESPONSE


async def test_time_series_start_end_only_success():
    with aioresponses() as m:
        m.get(
            url=f'{BASE_URL}/meter_reading/{EXAMPLE_DEVICE_ID}?'
            f'start=1706321700&end=1706321880',
            status=200,
            payload=EXAMPLE_TIME_SERIES_START_END_RESPONSE
        )

        async with ClientSession() as session:
            powerpal = Powerpal(session, EXAMPLE_AUTH_STR, EXAMPLE_DEVICE_ID)
            data = await powerpal.get_time_series_data(
                start=1706321700,
                end=1706321880
            )

        assert data == EXAMPLE_TIME_SERIES_START_END_RESPONSE


async def test_time_series_start_end_sample_success():
    with aioresponses() as m:
        m.get(
            url=f'{BASE_URL}/meter_reading/{EXAMPLE_DEVICE_ID}?'
            f'start=1706321820&end=1706332620&sample=60',
            status=200,
            payload=EXAMPLE_TIME_SERIES_START_END_SAMPLE_60_RESPONSE
        )

        async with ClientSession() as session:
            powerpal = Powerpal(session, EXAMPLE_AUTH_STR, EXAMPLE_DEVICE_ID)
            data = await powerpal.get_time_series_data(
                start=1706321820,
                end=1706332620,
                sample=60
            )

        assert data == EXAMPLE_TIME_SERIES_START_END_SAMPLE_60_RESPONSE


async def test_time_series_start_sample_only_success():
    with aioresponses() as m:
        m.get(
            url=f'{BASE_URL}/meter_reading/{EXAMPLE_DEVICE_ID}?'
            f'start=1706329020&sample=60',
            status=200,
            payload=EXAMPLE_TIME_SERIES_START_SAMPLE_60_RESPONSE
        )

        async with ClientSession() as session:
            powerpal = Powerpal(session, EXAMPLE_AUTH_STR, EXAMPLE_DEVICE_ID)
            data = await powerpal.get_time_series_data(
                start=1706329020,
                sample=60
            )

        assert data == EXAMPLE_TIME_SERIES_START_SAMPLE_60_RESPONSE


async def test_time_series_sample_only_success():
    with aioresponses() as m:
        m.get(
            url=f'{BASE_URL}/meter_reading/{EXAMPLE_DEVICE_ID}?'
            f'sample=60',
            status=200,
            payload=EXAMPLE_TIME_SERIES_SAMPLE_60_RESPONSE
        )

        async with ClientSession() as session:
            powerpal = Powerpal(session, EXAMPLE_AUTH_STR, EXAMPLE_DEVICE_ID)
            data = await powerpal.get_time_series_data(sample=60)

        assert data == EXAMPLE_TIME_SERIES_SAMPLE_60_RESPONSE


async def test_authentication_error():
    with aioresponses() as m:
        m.get(
            url=f'{BASE_URL}/device/{EXAMPLE_DEVICE_ID}',
            status=401,
            body="Authentication Error"
        )

        async with ClientSession() as session:
            powerpal = Powerpal(session, EXAMPLE_AUTH_STR, EXAMPLE_DEVICE_ID)
            with pytest.raises(PowerpalAuthenticationException):
                await powerpal.get_data()


async def test_authorization_error():
    with aioresponses() as m:
        m.get(
            url=f'{BASE_URL}/device/{EXAMPLE_DEVICE_ID}',
            status=403,
            body="Authorization Error"
        )

        async with ClientSession() as session:
            powerpal = Powerpal(session, EXAMPLE_AUTH_STR, EXAMPLE_DEVICE_ID)
            with pytest.raises(PowerpalAuthorizationException):
                await powerpal.get_data()


async def test_server_error():
    with aioresponses() as m:
        m.get(
            url=f'{BASE_URL}/device/{EXAMPLE_DEVICE_ID}',
            status=500,
            body="Server Error"
        )

        async with ClientSession() as session:
            powerpal = Powerpal(session, EXAMPLE_AUTH_STR, EXAMPLE_DEVICE_ID)
            with pytest.raises(PowerpalException):
                await powerpal.get_data()


async def test_timeout_error():
    with aioresponses() as m:
        m.get(
            url=f'{BASE_URL}/device/{EXAMPLE_DEVICE_ID}',
            exception=ServerTimeoutError()
        )

        async with ClientSession() as session:
            powerpal = Powerpal(session, EXAMPLE_AUTH_STR, EXAMPLE_DEVICE_ID)
            with pytest.raises(PowerpalException):
                await powerpal.get_data()
