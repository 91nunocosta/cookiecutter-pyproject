from python_package import __version__


def test_version():
    assert __version__ == "{{cookiecutter.project_version}}"
