# Cookiecuter for Python projects

[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/91nunocosta/cookiecutter-pyproject)](https://github.com/91nunocosta/cookiecutter-pyproject/releases)
[![GitHub](https://img.shields.io/github/license/91nunocosta/cookiecutter-pyproject)](https://github.com/91nunocosta/cookiecutter-pyproject/blob/master/LICENSE)
[![GitHub branch checks state](https://img.shields.io/github/checks-status/91nunocosta/cookiecutter-pyproject/master)](https://github.com/91nunocosta/cookiecutter-pyproject)
[![GitHub branch checks state](https://img.shields.io/github/checks-status/91nunocosta/prototype-python-library/master)](https://github.com/91nunocosta/prototype-python-library)

This repository provides a [cookiecutter](https://github.com/cookiecutter/cookiecutter)
for Python projects.
It generates the example project [91nunocosta/prototype-python-library](https://github.com/91nunocosta/prototype-python-library).

## Usage

To create a new Python project, run the following command, and answer all prompts.

```bash
cookiecutter https@github.com/91nunocosta/cookiecutter-pyproject.git
```

## Project types

The repository provides the following project types.

### Python API library

The Python API library template provides the following:

* [poetry](https://python-poetry.org/) setup
* [pre-commit](https://pre-commit.com/) configuration for linting with multiple linters
  (see [.pre-commit-config.yaml](./{{cookiecutter.package_name}}/.pre-commit-config.yaml))
* [tox](https://tox.wiki/en/latest/) configuration
* [GitHub workflows](https://docs.github.com/en/actions/using-workflows) to:
  * lint commit messages according to [Conventional Commit](https://www.conventionalcommits.org/en/v1.0.0/)
  * test with [tox](https://tox.wiki/en/latest/)
  * release the package with [Python Semantic Release](https://python-semantic-release.readthedocs.io/en/latest/)

### Contributing

If you want to contribute, please read the [contributing guidelines](./CONTRIBUTING.md)
and [code of conduct](./CODE_OF_CONDUCT.md).
