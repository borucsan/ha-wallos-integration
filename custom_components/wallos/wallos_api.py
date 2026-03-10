import aiohttp


class WallosAPI:

    def __init__(self, url, api_key):
        self.url = url.rstrip("/")
        self.api_key = api_key

    async def get_subscriptions(self):

        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        async with aiohttp.ClientSession() as session:

            async with session.get(
                f"{self.url}/api/subscriptions",
                headers=headers,
            ) as resp:

                resp.raise_for_status()
                return await resp.json()