# -*- coding: utf-8 -*-
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.rst")).read()

setup(
    name="nmea-kindle-panel",
    version="0.0.0",
    author="Andreas Motl",
    author_email="andreas.motl@panodata.org",
    url="https://git.cicer.de/karatefish/nmea-kindle-panel",
    description="Converge a kindle into a display panel for NMEA and SignalK telemetry data",
    long_description=README,
    download_url="https://pypi.org/project/nmea-kindle-panel/",
    packages=find_packages(),
    license="AGPL-3.0, EUPL-1.2",
    keywords=[
        "display",
        "panel",
        "kindle",
        "nmea",
        "nmea-0183",
        "navigation",
        "sensor",
        "opencpn",
        "signalk",
        "openplotter",
        "environmental-monitoring",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)",
        "Development Status :: 4 - Beta",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Natural Language :: English",
        "Intended Audience :: Customer Service",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
        "Topic :: Communications",
        "Topic :: Education :: Testing",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
        "Topic :: Scientific/Engineering",
        "Topic :: System :: Emulators",
        "Topic :: System :: Networking",
        "Topic :: Utilities",
    ],
    entry_points={
        "console_scripts": [
            "nmea-kindle-panel = nmea_kindle_panel.cli:cli",
        ],
    },
    install_requires=[
        "pynmea2>1,<2",
        "click<9",
        "dataclasses;python_version<='3.6'",
    ],
    extras_require={
        "test": [
            "pytest<8",
            "pytest-cov<4",
        ],
    },
)
