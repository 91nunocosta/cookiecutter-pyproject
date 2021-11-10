from {{cookiecutter.module_name}} import __version__


def test_version():
    assert __version__ == "{{cookiecutter.package_version}}"
