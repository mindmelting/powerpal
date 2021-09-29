from aiohttp import ClientSession, ClientResponseError
from .exceptions import (
    PowerpalException,
    PowerpalAuthorizationException,
    PowerpalAuthenticationException
)

BASE_URL = "https://readings.powerpal.net"


class Powerpal:
    def __init__(self, session: ClientSession, authKey: str, deviceId: str):
        self._session = session
        self._authKey = authKey
        self._deviceId = deviceId

    async def get_data(self):
        headers = {
            "Accept": "application/json",
            "Accept-Language": "en-au",
            "Authorization": self._authKey,
            "User-Agent": "Powerpal/1936 CFNetwork/1240.0.4 Darwin/20.6.0",
        }
        try:
            resp = await self._session.get(
                f"${BASE_URL}/api/v1/device/{self._deviceId}",
                headers=headers,
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
