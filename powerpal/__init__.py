from aiohttp import ClientSession


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
        resp = await self._session.get(
            f"https://readings.powerpal.net/api/v1/device/{self._deviceId}",
            headers=headers,
            raise_for_status=True
        )

        data = await resp.json(content_type=None)

        return data
