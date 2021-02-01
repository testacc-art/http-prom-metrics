from http import HTTPStatus

from asynctest import TestCase
from asyncworker.testing import HttpClientContext

from httpmetrics import app


class EchoEndpointTest(TestCase):
    async def test_returns_200_ok(self):
        async with HttpClientContext(app) as client:
            resp = await client.get("/echo/10")
            self.assertEqual(HTTPStatus.OK, resp.status)

            data = await resp.json()
            self.assertEqual({"value": 10, "x2": 20}, data)
