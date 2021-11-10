"nox configuration." ""
import nox_poetry


PYTHON_VERSIONS = ["3.9"]
SRC_DIR = "python_package"
TEST_COVERAGE = 100


@nox_poetry.session()
def lint(session):
    """Lint the source code."""
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files")


@nox_poetry.session()
def tests(session):
    """Test."""
    session.install(".")
    session.install("pytest")
    session.install("pytest-cov")
    session.install("coverage-badge")
    session.install("nox-poetry")

    session.run(
        "pytest",
        f"--cov-fail-under={TEST_COVERAGE}",
        f"--cov={SRC_DIR}",
        "--doctest-modules",
        "--doctest-glob=README.md",
    )

    session.run("coverage-badge", "-f", "-o", "coverage.svg")
