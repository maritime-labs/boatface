# -*- coding: utf-8 -*-
# (c) 2022 Holger Marseille <ml@argonauta.studio>
# (c) 2022 Andreas Motl <andreas.motl@panodata.org>
# License: GNU Affero General Public License, Version 3
import asyncio
import logging
import queue
import threading

import asyncio_dgram
import pynmea2

from boatface.model import DataValues
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


class UdpNmeaMessageForwarder(threading.Thread):

    def __init__(self):
        super().__init__()
        self.queue: queue.Queue = queue.Queue()

    def run(self):
        """
        asyncio + multithreading: one asyncio event loop per thread.

        https://gist.github.com/lars-tiede/01e5f5a551f29a5f300e
        """
        logger.info("Starting UdpNmeaMessageForwarder thread")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.worker())
        loop.close()

    async def worker(self):
        logger.info("Starting UdpNmeaMessageForwarder worker task")
        receiver = UdpNmeaMessageReceiver()
        async for message in receiver.read():
            logger.info(f"Decoded message: {dict(message)}")
            data = DataValues(awa=message["deg_r"], aws=message["wind_speed_kn"])
            logger.info(f"Queuing data: {data}")
            self.queue.put(data, block=False)
