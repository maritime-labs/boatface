# -*- coding: utf-8 -*-
# (c) 2022 Andreas Motl <andreas.motl@panodata.org>
# License: GNU Affero General Public License, Version 3
from copy import deepcopy

from boatface.model import RenderValues
from testing.conf import test_reading


def test_rendervalues():
    data = deepcopy(test_reading)
    tplvars = RenderValues.from_data(data)
    assert tplvars == RenderValues(
        cog="42.4", sog="4.3", dbt="84.8", hdg="5.8", awa="42", aws="4.2", twa="170", tws="6.2"
    )
