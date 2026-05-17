"""
NoiseForge
===========

A lightweight procedural noise generation toolkit written in pure Python.

NoiseForge focuses on deterministic grayscale noise synthesis with
minimal dependencies and fully manual PNG exporting.

The project is designed to be:

- Lightweight
- Portable
- Dependency-free
- Deterministic
- Easy to extend
- Educational

Core Features
--------------

- Seeded deterministic noise generation
- Repeatable/tileable pattern support
- Adjustable grayscale ranges
- Pure Python PNG encoding
- Tkinter graphical interface
- Fully offline operation

Architecture
------------

NoiseForge is separated into multiple modules:

generator
    Handles deterministic noise generation logic.

pngwriter
    Encodes and exports grayscale PNG files.

ui
    Provides the graphical user interface.

Future modules may include:

- animation
- gradients
- perlin noise
- simplex noise
- shaders
- GPU acceleration
- batch exporters

Execution
---------

NoiseForge can be started using:

    python -m noiseforge

Metadata
--------

Author:
    Spakerdev

Project:
    NoiseForge

License:
    MIT License
Version:
    Alpha 0.0.1
"""

from noiseforge.generator import (
    deterministicnoise,
    generatenoise
)

from noiseforge.pngwriter import (
    createchunk,
    savepng
)

__version__ = "Alpha 0.0.1"

__author__ = "Spakerdev"

__license__ = "MIT License"

__all__ = [
    "deterministicnoise",
    "generatenoise",
    "createchunk",
    "savepng"
]


def get_version():
    return __version__


def get_author():
    return __author__


def initialize():
    """
    Initialize NoiseForge package state.

    Future initialization systems may include:

    - plugin loading
    - configuration loading
    - cache initialization
    - renderer registration
    - backend selection

    Returns
    -------
    dict
        Basic package information.
    """

    return {
        "name": "NoiseForge",
        "version": __version__,
        "author": __author__,
        "initialized": True
    }


PACKAGE_INFO = initialize()
