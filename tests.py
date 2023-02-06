"""Test python-package-cookiecuter."""
import subprocess
from typing import List


def test_scoffold_base_package(cookies):
    """Test scaffolding a minimal Python package."""
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

    run(["git", "init"])
    run(["poetry", "install"])
    run(["poetry", "run", "pre-commit", "run", "--all-files"])
    run(["poetry", "run", "tox"])
