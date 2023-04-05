"""Test python-package-cookiecuter."""
import subprocess
from typing import List

import pytest


@pytest.mark.parametrize(
    "extra_context",
    [{"opensource": "no"}, {"cli": "no"}],
    ids=[
        "non-opensource",
        "without cli",
    ],
)
def test_linting(cookies, extra_context):
    """Test scaffolding and then linting."""
    result = cookies.bake(extra_context=extra_context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "template-pyproject"
    assert result.project_path.is_dir()
    print("scaffold finished!")

    def run(command: List[str]):
        print(" ".join(command))
        command_result = subprocess.run(command, cwd=result.project_path.absolute())
        assert command_result.returncode == 0, command_result.stderr

    run(["git", "init"])
    run(["poetry", "check"])
    run(["poetry", "install", "--with=lint"])
    run(["git", "add", "."])
    run(["poetry", "run", "pre-commit", "run", "--all-files"])


def test_testing(cookies):
    """Test scaffolding a minimal Python package and then testing."""
    result = cookies.bake()
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "template-pyproject"
    assert result.project_path.is_dir()
    print("scaffold finished!")

    def run(command: List[str]):
        print(" ".join(command))
        command_result = subprocess.run(command, cwd=result.project_path.absolute())
        assert command_result.returncode == 0

    run(["poetry", "install", "--with=cd"])
    run(["poetry", "run", "tox"])
    run(["poetry", "run", "template-pyproject", "10"])
