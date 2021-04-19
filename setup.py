"""
doreentd 

The doreentd project is an open-source quantitative trading framework
that developed based on two other open-source quantitative trading
project: pyalgotrade and vn.py.

The project is mainly written in Python and uses C++ for low-layer
and performance sensitive infrastructure.

"""

import ast
import re
import sys

from setuptools import find_packages, setup


def get_install_requires():
    install_requires = [
        "six==1.13.0",
        "wheel",
        "PyQt5==5.15.2",
        "pyqtgraph==0.10.0",
        "qdarkstyle",
        "requests",
        "websocket-client",
        "peewee",
        "pymysql",
        "mongoengine",
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "deap",
        "tzlocal==2.1",
        "plotly",
        "pandas_ta",
		"tzdata"
    ]

    if sys.version_info.minor < 7:
        install_requires.append("dataclasses")
    return install_requires


def get_version_string():
    global version
    with open("doreentd/__init__.py", "rb") as f:
        version_line = re.search(
            r"__version__\s+=\s+(.*)", f.read().decode("utf-8")
        ).group(1)
        return str(ast.literal_eval(version_line))

setup(
    name="doreentd",
    version=get_version_string(),
    author="vn.py team, Gabriel, Bo",
    author_email="305545659@qq.com",
    license="MIT",
    url="https://www.vnpy.com https://gbeced.github.io/pyalgotrade/",
    description="A framework for developing quant trading systems.",
    long_description=__doc__,
    keywords='quant quantitative investment trading algotrading',
    include_package_data=True,
    packages=find_packages(exclude=["tests", "ci", "tests.*"]),
    package_data={"": [
        "*.ico",
        "*.ini",
        "*.dll",
        "*.so",
        "*.pyd",
    ]},
    install_requires=get_install_requires(),
	extras_require={
        "TALib":  ["Cython", "TA-Lib"],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Operating System :: Microsoft :: Windows :: Windows 8",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows Server 2008",
        "Operating System :: Microsoft :: Windows :: Windows Server 2012",
        "Operating System :: Microsoft :: Windows :: Windows Server 2012",
        "Operating System :: POSIX :: Linux"
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Office/Business :: Financial :: Investment :: 51bitquant",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: Chinese (Simplified)"
    ],
)
