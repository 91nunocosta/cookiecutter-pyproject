from pathlib import Path
from typing import List

OPENSOURCE_FILES: List[Path] = [
    Path("CODE_OF_CONDUCT.md"),
    Path("CONTRIBUTING.md"),
    Path("LICENSE"),
    Path(".markdownlintignore"),
    Path(".github/workflows/commitlint.yml"),
    Path(".github/workflows/release_package.yml"),
    Path(".github/workflows/docs.yml"),
]
CLI_FILES: List[Path] = [
    Path(".") / "{{ cookiecutter.module_name }}" / "cli.py",
    Path(".") / "tests" / "test_cli.py",
]

def remove(paths: List[Path]) -> None:
    for path in paths:
        if path.is_dir():
            path.rmdir()
        else:
            path.unlink()

{% if cookiecutter.opensource != "yes" %}remove(OPENSOURCE_FILES) {% endif %}
{% if cookiecutter.cli != "yes" %}remove(CLI_FILES) {% endif %}
