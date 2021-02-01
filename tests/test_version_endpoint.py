import os
from http import HTTPStatus

from asynctest import mock, TestCase
from asyncworker.testing import HttpClientContext

from httpmetrics import app


class VersionEndpointTest(TestCase):
    async def test_returns_200_ok(self):
        async with HttpClientContext(app) as client:
            resp = await client.get("/_version")
            self.assertEqual(HTTPStatus.OK, resp.status)

            data = await resp.json()
            self.assertEqual({"git-commit": "", "git-tag-ref": ""}, data)

    async def test_return_values_if_env_exist(self):
        git_commit = "some-hash"
        git_tag_ref = "feature/some-branch"
        with mock.patch.dict(
            os.environ, GIT_COMMIT=git_commit, GIT_TAGREF=git_tag_ref
        ) as var:
            async with HttpClientContext(app) as client:
                resp = await client.get("/_version")
                self.assertEqual(HTTPStatus.OK, resp.status)

                data = await resp.json()
                self.assertEqual(
                    {"git-commit": git_commit, "git-tag-ref": git_tag_ref}, data
                )
