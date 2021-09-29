import pytest
from aiohttp import ClientSession, ClientResponseError, ServerTimeoutError

from aioresponses import aioresponses

from powerpal import Powerpal
from powerpal.exceptions import (
    PowerpalException,
    PowerpalAuthorizationException,
    PowerpalAuthenticationException
)

EXAMPLE_RESPONSE = {
    "serial_number": "1234",
    "total_meter_reading_count": 28000,
    "total_watt_hours": 124000,
    "total_cost": 325,
    "first_reading_timestamp": 1615521060,
    "last_reading_timestamp": 1632810120,
    "last_reading_watt_hours": 2,
    "last_reading_cost": 0.0011875,
    "available_days": 200
}

EXAMPLE_DEVICE_ID = "12345"
EXAMPLE_AUTH_STR = "abcd"


async def test_success():
    with aioresponses() as m:
        m.get(
            f'https://readings.powerpal.net/api/v1/device/{EXAMPLE_DEVICE_ID}',
            status=200, payload=EXAMPLE_RESPONSE)

        session = ClientSession()
        powerpal = Powerpal(session, EXAMPLE_AUTH_STR, EXAMPLE_DEVICE_ID)
        data = await powerpal.get_data()

        assert data == EXAMPLE_RESPONSE


async def test_authentication_error():
    with aioresponses() as m:
        m.get(
            f'https://readings.powerpal.net/api/v1/device/{EXAMPLE_DEVICE_ID}',
            status=401, body="Authentication Error")

        session = ClientSession()
        powerpal = Powerpal(session, EXAMPLE_AUTH_STR, EXAMPLE_DEVICE_ID)
        with pytest.raises(PowerpalAuthenticationException):
            await powerpal.get_data()


async def test_authorization_error():
    with aioresponses() as m:
        m.get(
            f'https://readings.powerpal.net/api/v1/device/{EXAMPLE_DEVICE_ID}',
            status=403, body="Authentication Error")

        session = ClientSession()
        powerpal = Powerpal(session, EXAMPLE_AUTH_STR, EXAMPLE_DEVICE_ID)
        with pytest.raises(PowerpalAuthorizationException):
            await powerpal.get_data()


async def test_server_error():
    with aioresponses() as m:
        m.get(
            f'https://readings.powerpal.net/api/v1/device/{EXAMPLE_DEVICE_ID}',
            status=500, body="Server Error")

        session = ClientSession()
        powerpal = Powerpal(session, EXAMPLE_AUTH_STR, EXAMPLE_DEVICE_ID)
        with pytest.raises(PowerpalException):
            await powerpal.get_data()


async def test_timeout_error():
    with aioresponses() as m:
        m.get(
            f'https://readings.powerpal.net/api/v1/device/{EXAMPLE_DEVICE_ID}',
            exception=ServerTimeoutError())

        session = ClientSession()
        powerpal = Powerpal(session, EXAMPLE_AUTH_STR, EXAMPLE_DEVICE_ID)
        with pytest.raises(PowerpalException):
            await powerpal.get_data()
