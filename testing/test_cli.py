import re

from click.testing import CliRunner

from boatface.cli import cli


def test_cli_version():
    """Test boatface --version"""
    runner = CliRunner()

    result = runner.invoke(cli, ["--version"])

    assert re.match(r"cli, version \d+\.\d+\.\d+", result.stdout) is not None
