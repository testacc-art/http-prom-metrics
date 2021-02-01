from os import path

from setuptools import (  # Always prefer setuptools over distutils
    find_packages,
    setup,
)

here = path.abspath(path.dirname(__file__))

setup(
    name="http-prom-metrics",
    version="0.1.0",
    description="Exemplo de métricas para Prometheus",
    long_description="",
    url="https://github.com/daltonmatos/http-prom-metrics",
    author="Dalton Matos",
    author_email="daltonmatos@gmail.com",
    license="MIT",
    classifiers=["Programming Language :: Python :: 3.8"],
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    test_suite="tests",
    install_requires=[],
    entry_points={},
)
