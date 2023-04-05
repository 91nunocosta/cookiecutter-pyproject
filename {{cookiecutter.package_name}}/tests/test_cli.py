"""Test the command line interface for {{ cookiecutter.module_name }}."""
from typer.testing import CliRunner

from {{ cookiecutter.module_name }}.cli import app

runner = CliRunner()


def test_app() -> None:
    """Test the command line interface for {{ cookiecutter.module_name }}"""
    result = runner.invoke(app, ["10"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "55"
