# -*- coding: utf-8 -*-
# (c) 2022 Andreas Motl <andreas.motl@panodata.org>
# License: GNU Affero General Public License, Version 3
import logging
import re
import shlex
from unittest import mock

from click.testing import CliRunner

from boatface.cli import cli


def test_cli_version():
    """
    Test `boatface --version`
    """
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert re.match(r"cli, version \d+\.\d+\.\d+", result.stdout) is not None


@mock.patch("PIL.Image._show")
def test_cli_ui_viewer_portrait(_, caplog):
    """
    Test `boatface ui --source=demo:// --display=viewer`
    """
    runner = CliRunner()
    result = runner.invoke(cli, shlex.split("ui --source=demo:// --display=viewer"))
    assert result.stdout == ""
    assert "Drawing frame finished" in caplog.messages


@mock.patch("PIL.Image._show")
def test_cli_ui_viewer_landscape(_, caplog):
    """
    Test `boatface ui --source=demo:// --display=viewer --landscape`
    """
    runner = CliRunner()
    result = runner.invoke(cli, shlex.split("ui --source=demo:// --display=viewer --landscape"))
    assert result.stdout == ""
    assert "Drawing frame finished" in caplog.messages
