from http import HTTPStatus

from asynctest import TestCase
from asyncworker.testing import HttpClientContext

from httpmetrics import app, alert_test


class ExampleMetricEndpointTest(TestCase):
    async def test_warning_example_metric_value_0(self):
        priority = "warning"
        value = 0
        async with HttpClientContext(app) as client:
            resp = await client.get(f"/{priority}/{value}")
            self.assertEqual(HTTPStatus.OK, resp.status)

            data = await resp.json()
            self.assertEqual({"priority": priority, "value": value}, data)

            metric = alert_test.collect()
            self.assertEqual(1, len(metric))

            samples = [
                sample
                for sample in metric[0].samples
                if sample.labels == {"priority": priority}
            ]
            self.assertEqual(1, len(samples))
            self.assertEqual(value, samples[0].value)

    async def test_warning_example_metric_value_1(self):
        priority = "warning"
        value = 1
        async with HttpClientContext(app) as client:
            resp = await client.get(f"/{priority}/{value}")
            self.assertEqual(HTTPStatus.OK, resp.status)

            data = await resp.json()
            self.assertEqual({"priority": priority, "value": value}, data)

            metric = alert_test.collect()
            self.assertEqual(1, len(metric))

            samples = [
                sample
                for sample in metric[0].samples
                if sample.labels == {"priority": priority}
            ]
            self.assertEqual(1, len(samples))
            self.assertEqual(value, samples[0].value)

    async def test_critical_example_metric_value_0(self):
        priority = "critical"
        value = 0
        async with HttpClientContext(app) as client:
            resp = await client.get(f"/{priority}/{value}")
            self.assertEqual(HTTPStatus.OK, resp.status)

            data = await resp.json()
            self.assertEqual({"priority": priority, "value": value}, data)

            metric = alert_test.collect()
            self.assertEqual(1, len(metric))

            samples = [
                sample
                for sample in metric[0].samples
                if sample.labels == {"priority": priority}
            ]
            self.assertEqual(1, len(samples))
            self.assertEqual(value, samples[0].value)

    async def test_critical_example_metric_value_1(self):
        priority = "critical"
        value = 1
        async with HttpClientContext(app) as client:
            resp = await client.get(f"/{priority}/{value}")
            self.assertEqual(HTTPStatus.OK, resp.status)

            data = await resp.json()
            self.assertEqual({"priority": priority, "value": value}, data)

            metric = alert_test.collect()
            self.assertEqual(1, len(metric))

            samples = [
                sample
                for sample in metric[0].samples
                if sample.labels == {"priority": priority}
            ]
            self.assertEqual(1, len(samples))
            self.assertEqual(value, samples[0].value)
