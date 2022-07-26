# -*- coding: utf-8 -*-
# (c) 2022 Andreas Motl <andreas.motl@panodata.org>
# License: GNU Affero General Public License, Version 3
import io
from copy import deepcopy

from boatface.model import RenderValues
from boatface.render import FrameRenderer
from testing.conf import test_reading


def test_render_png():
    data = deepcopy(test_reading)
    tplvars = RenderValues.from_data(data)
    renderer = FrameRenderer()
    buffer = renderer.render_png(tplvars)
    assert isinstance(buffer, io.BytesIO)
    assert buffer.read(4) == b"\x89PNG"


def test_render_low_dbt():
    data = deepcopy(test_reading)
    data.dbt = 0.2
    tplvars = RenderValues.from_data(data)
    renderer = FrameRenderer()
    buffer = renderer.render_png(tplvars)
    assert isinstance(buffer, io.BytesIO)
    assert buffer.read(4) == b"\x89PNG"
