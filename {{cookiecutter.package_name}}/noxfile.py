"""nox configuration."""
from pathlib import Path

import nox
from poetry.core.pyproject.toml import PyProjectTOML

PROJECT = PyProjectTOML(Path.cwd() / "pyproject.toml").poetry_config

PROJECT_NAME = PROJECT["name"]
PROJECT_VERSION = PROJECT["version"]

SRC_DIR = PROJECT_NAME.replace("-", "_")

TEST_COVERAGE = 100


@nox.session(python=None, reuse_venv=True)
def check(session):
    """Lint the source code."""
    session.install("poetry")
    session.run("poetry", "run", "pre-commit", "run", "--all-files", external=True)


@nox.session(python=None, reuse_venv=True)
def build(session):
    """Build the package from the source code."""
    session.install("poetry")
    session.run("poetry", "build", "-f", "wheel")


@nox.session(python="3.9")
def tests_package(session):
    """Test package."""
    session.install(f"./dist/{SRC_DIR}-{PROJECT_VERSION}-py3-none-any.whl")
    session.install("pytest")
    session.run("pytest", "tests/")
