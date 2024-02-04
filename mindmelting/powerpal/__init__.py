from aiohttp import ClientSession, ClientResponseError
from urllib import parse
from .exceptions import (
    PowerpalException,
    PowerpalAuthorizationException,
    PowerpalAuthenticationException
)

BASE_URL = "https://readings.powerpal.net"


class Powerpal:
    def __init__(self, session: ClientSession, authKey: str, deviceId: str):
        self._session = session
        self._deviceId = deviceId
        self._headers = {
            "Accept": "application/json",
            "Accept-Language": "en-au",
            "Authorization": authKey,
            "User-Agent": "Powerpal/1936 CFNetwork/1240.0.4 Darwin/20.6.0",
        }

    async def get_data(self):
        try:
            url = f"{BASE_URL}/api/v1/device/{self._deviceId}"
            resp = await self._session.get(
                url=url,
                headers=self._headers,
                raise_for_status=True
            )
        except (ClientResponseError) as error:
            if error.status == 401:
                raise PowerpalAuthenticationException(
                    "Authentication error. Ensure valid auth key is used")
            if error.status == 403:
                raise PowerpalAuthorizationException(
                    "Authorization error. Ensure valid device id is used")
            else:
                raise PowerpalException(f'[{error.status}]: {error.message}')
        except (Exception) as error:
            raise PowerpalException(error)

        data = await resp.json(content_type=None)

        return data

    async def get_time_series_data(
        self,
        start: int = None,
        end: int = None,
        sample: int = None
    ):
        def build_params():
            params = {}
            if start is not None:
                params.update(start=start)
            if end is not None:
                params.update(end=end)
            if sample is not None:
                params.update(sample=sample)
            return params

        try:
            url_params = build_params()
            url = (f"{BASE_URL}/api/v1/meter_reading/{self._deviceId}" + (
                ("?" + parse.urlencode(url_params)) if url_params else ""))
            resp = await self._session.get(
                url=url,
                headers=self._headers,
                raise_for_status=True
            )
        except (ClientResponseError) as error:
            if error.status == 401:
                raise PowerpalAuthenticationException(
                    "Authentication error. Ensure valid auth key is used")
            if error.status == 403:
                raise PowerpalAuthorizationException(
                    "Authorization error. Ensure valid device id is used")
            else:
                raise PowerpalException(f'[{error.status}]: {error.message}')
        except (Exception) as error:
            raise PowerpalException(error)

        data = await resp.json(content_type=None)

        return data
