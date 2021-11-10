"""nox configuration."""
from pathlib import Path

import nox_poetry


PYTHON_VERSIONS = ["3.9"]
SRC_DIR = Path(__file__).parent.name
TEST_COVERAGE = 100


@nox_poetry.session()
def lint(session):
    """Lint the source code."""
    # start_poetry(session)
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files")


@nox_poetry.session()
def tests(session):
    """Test."""
    # start_poetry(session)
    session.install(".")
    session.install("pytest")
    session.install("pytest-cov")
    session.install("coverage-badge")
    session.run("pytest", f"--cov-fail-under={TEST_COVERAGE}", "--cov", "tests/")
    session.run("coverage-badge", "-f", "-o", "coverage.svg")
