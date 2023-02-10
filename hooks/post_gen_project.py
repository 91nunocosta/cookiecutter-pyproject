from pathlib import Path
from typing import List

OPENSOURCE_FILES: List[Path] = [
    Path("CODE_OF_CONDUCT.md"),
    Path("LICENSE"),
]

def remove(paths: List[Path]) -> None:
    for path in paths:
        if path.is_dir():
            path.rmdir()
        else:
            path.unlink()

{% if cookiecutter.opensource != "yes" %}remove(OPENSOURCE_FILES) {% endif %}
