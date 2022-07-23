# -*- coding: utf-8 -*-
# (c) 2022 Andreas Motl <andreas.motl@panodata.org>
# License: GNU Affero General Public License, Version 3
import logging
import sys

import click

from nmea_kindle_panel.core import UdpNmeaMessageReceiver
from nmea_kindle_panel.util import make_sync, setup_logging

logger = logging.getLogger(__name__)


@click.group()
@click.version_option()
@click.option("--verbose", is_flag=True, required=False, help="Increase log verbosity.")
@click.option("--debug", is_flag=True, required=False, help="Enable debug messages.")
@click.pass_context
def cli(ctx, verbose, debug):
    setup_logging(level=logging.DEBUG)


@click.command()
@click.option("--source", type=str, required=False, help="Receive telemetry data from source")
@click.pass_context
@make_sync
async def log(ctx, source: str):
    receiver = UdpNmeaMessageReceiver()
    async for message in receiver.read():
        logger.info(f"Decoded message: {dict(message)}")
    print("Ready.", file=sys.stderr)


cli.add_command(log, name="log")
