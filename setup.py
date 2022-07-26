# -*- coding: utf-8 -*-
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.rst")).read()

setup(
    name="boatface",
    version="0.0.2",
    author="Holger Marseille",
    author_email="ml@argonauta.studio",
    maintainer="Andreas Motl",
    maintainer_email="andreas.motl@panodata.org",
    url="https://github.com/maritime-labs/boatface",
    description="Instrumentation panel for displaying NMEA and SignalK telemetry data",
    long_description=README,
    download_url="https://pypi.org/project/boatface/",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "boatface": [
            "assets/*.png",
            "assets/*.otf",
        ],
    },
    license="AGPL-3.0, EUPL-1.2",
    keywords=[
        "instrumentation",
        "navigation",
        "panel",
        "display",
        "opencpn",
        "signalk",
        "openplotter",
        "nmea",
        "nmea-0183",
        "sailing",
        "sensor",
        "environmental-monitoring",
        "e-ink",
        "kindle",
        "kobo",
        "tolino",
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
        "Development Status :: 3 - Alpha",
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
        "Topic :: Scientific/Engineering",
        "Topic :: System :: Emulators",
        "Topic :: System :: Networking",
        "Topic :: Utilities",
    ],
    entry_points={
        "console_scripts": [
            "boatface = boatface.cli:cli",
        ],
    },
    install_requires=[
        "asyncio-dgram>2,<3",
        "pynmea2>1,<2",
        "Pillow<10",
        "click<9",
        "dataclasses;python_version<='3.6'",
        "importlib_metadata;python_version<='3.7'",
    ],
    extras_require={
        "ui": [
            "pyglet<2",
            "pysdl2<1",
        ],
        "test": [
            "pytest<8",
            "pytest-cov<4",
        ],
    },
)
