"""Test python-package-cookiecuter."""
import subprocess
from typing import List

import pytest


@pytest.mark.parametrize(
    "extra_context",
    [{"opensource": "no"}, {"cli": "no"}],
    ids=["non-opensource", "without cli"],
)
def test_scaffolding(cookies, extra_context):
    """Test scaffolding a minimal Python package."""
    result = cookies.bake(extra_context=extra_context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "prototype-python-library"
    assert result.project_path.is_dir()
    print("scaffold finished!")


@pytest.mark.parametrize(
    "extra_context",
    [{"opensource": "no"}, {"cli": "no"}],
    ids=[
        "non-opensource",
        "without cli",
    ],
)
def test_linting(cookies, extra_context):
    """Test scaffolding a minimal Python package and then linting."""
    result = cookies.bake(extra_context=extra_context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "prototype-python-library"
    assert result.project_path.is_dir()
    print("scaffold finished!")

    def run(command: List[str]):
        print(" ".join(command))
        command_result = subprocess.run(command, cwd=result.project_path.absolute())
        assert command_result.returncode == 0, command_result.stderr

    run(["git", "init"])
    run(["poetry", "check"])
    run(["poetry", "install"])
    run(["git", "add", "."])
    run(["poetry", "run", "pre-commit", "run", "--all-files"])


def test_testing(cookies):
    """Test scaffolding a minimal Python package and then testing."""
    result = cookies.bake()
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "prototype-python-library"
    assert result.project_path.is_dir()
    print("scaffold finished!")

    def run(command: List[str]):
        print(" ".join(command))
        command_result = subprocess.run(command, cwd=result.project_path.absolute())
        assert command_result.returncode == 0

    run(["poetry", "install"])
    run(["poetry", "run", "tox"])


def test_run_command(cookies):
    """Test scaffolding the Python package and then running the cli."""
    result = cookies.bake()
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "prototype-python-library"
    assert result.project_path.is_dir()
    print("scaffold finished!")

    def run(command: List[str]):
        print(" ".join(command))
        command_result = subprocess.run(command, cwd=result.project_path.absolute())
        assert command_result.returncode == 0

    run(["poetry", "install"])
    run(["poetry", "run", "prototype-python-library", "10"])
