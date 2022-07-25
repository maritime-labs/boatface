# -*- coding: utf-8 -*-
# (c) 2022 Holger Marseille <ml@argonauta.studio>
# (c) 2022 Andreas Motl <andreas.motl@panodata.org>
# License: GNU Affero General Public License, Version 3
import logging

import asyncio_dgram
import pynmea2

from boatface.util import nmea_asdict

logger = logging.getLogger(__name__)


class UdpNmeaMessageReceiver:
    async def read_udp(self):
        # TODO: Parameterize hostname and port.
        stream = await asyncio_dgram.bind(("0.0.0.0", 10110))
        while True:
            data, remote_addr = await stream.recv()
            yield data, remote_addr

    async def read(self):
        async for data, remote_addr in self.read_udp():
            message = pynmea2.parse(data.decode())
            if message.sentence_type == "VWR":
                logger.info(f"Received VWR message: {message}")
            else:
                logger.warning(f"Received unknown message: {message}")
            msg = nmea_asdict(message)
            yield msg
