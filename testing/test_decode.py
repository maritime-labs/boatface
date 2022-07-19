# -*- coding: utf-8 -*-
# (c) 2022 Andreas Motl <andreas.motl@panodata.org>
# License: GNU Affero General Public License, Version 3
import pynmea2
from pynmea2 import VWR


def test_decode_nmea0183_vwr():
    sentence = "$IIVWR,154.0,L,11.06,N,5.69,M,20.48,K*65"
    msg = pynmea2.parse(sentence)
    assert msg.render() == VWR("II", "VWR", "154.0,L,11.06,N,5.69,M,20.48,K".split(",")).render()
