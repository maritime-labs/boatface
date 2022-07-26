# -*- coding: utf-8 -*-
# (c) 2022 Holger Marseille <ml@argonauta.studio>
# (c) 2022 Andreas Motl <andreas.motl@panodata.org>
# License: GNU Affero General Public License, Version 3
import logging
import sys

import click

from boatface.core import UdpNmeaMessageReceiver
from boatface.model import DataValues, DisplayBackend
from boatface.util import EnumChoice, make_sync, setup_logging

logger = logging.getLogger(__name__)


@click.group()
@click.version_option()
@click.option("--verbose", is_flag=True, required=False, help="Increase log verbosity.")
@click.option("--debug", is_flag=True, required=False, help="Enable debug messages.")
@click.pass_context
def cli(ctx, verbose, debug):
    log_level = logging.INFO
    if verbose or debug:
        log_level = logging.DEBUG
    setup_logging(level=log_level)


@click.command()
@click.option("--source", type=str, required=True, help="Receive telemetry data from source.")
@click.pass_context
@make_sync
async def log(ctx, source: str):
    receiver = UdpNmeaMessageReceiver()
    async for message in receiver.read():
        logger.info(f"Decoded message: {dict(message)}")
    print("Ready.", file=sys.stderr)


@click.command()
@click.option("--source", type=str, required=True, help="Receive telemetry data from source.")
@click.option(
    "--display",
    type=EnumChoice(DisplayBackend, case_sensitive=False),
    required=True,
    help="Render display with selected backend",
)
@click.option(
    "--landscape", is_flag=True, type=bool, required=False, default=False, help="Render output in landscape orientation"
)
@click.pass_context
@make_sync
async def ui(ctx, source: str, display: DisplayBackend, landscape: bool):
    if source == "demo://":
        data = DataValues(cog=42.42, dbt=84.84, sog=4.3, hdg=5.82, awa=42, aws=4.2, twa=170, tws=6.2)
    else:
        raise NotImplementedError(f"Selected data source {source} not implemented")

    if landscape and display not in [DisplayBackend.VIEWER, DisplayBackend.EIPS]:
        logger.warning(f"Option --landscape has no effect with display backend {display}")

    display_backend_class = DisplayBackend.get_implementer(display)

    app = display_backend_class(data=data, landscape=landscape)
    app.run()


cli.add_command(log, name="log")
cli.add_command(ui, name="ui")
