import os

from aiohttp.web import json_response
from asyncworker import App
from asyncworker.http.decorators import parse_path
from asyncworker.metrics import Gauge

alert_test = Gauge(
    "alert_test",
    "Metrica para validar alertas do Prometheus com Opsgenie",
    labelnames=["priority"],
)


app = App()


@app.http.get(["/other"])
async def _other():
    a = 1
    return json_response({})


@app.http.get(["/echo/{value}"])
@parse_path
async def echo(value: int):
    return json_response({"value": value, "x2": value * 2})


@app.http.get(["/_version"])
async def _version():
    GIT_COMMIT = os.getenv("GIT_COMMIT", "")
    GIT_TAGREF = os.getenv("GIT_TAGREF", "")
    return json_response({"git-commit": GIT_COMMIT, "git-tag-ref": GIT_TAGREF})


@app.http.get(["/other/path"])
async def other():
    return json_response({})


@app.http.get(["/{priority}/{value}"])
@parse_path
async def _ping(value: int, priority: str):
    alert_test.labels(priority=priority).set(value)
    return json_response({"priority": priority, "value": value})
