# Cookiecuter for Python projects

[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/91nunocosta/cookiecutter-pyproject)](https://github.com/91nunocosta/cookiecutter-pyproject/releases)
[![GitHub](https://img.shields.io/github/license/91nunocosta/cookiecutter-pyproject)](https://github.com/91nunocosta/cookiecutter-pyproject/blob/master/LICENSE)
[![GitHub branch checks state](https://img.shields.io/github/checks-status/91nunocosta/cookiecutter-pyproject/master)](https://github.com/91nunocosta/cookiecutter-pyproject)
[![GitHub branch checks state](https://img.shields.io/github/checks-status/91nunocosta/template-pyproject/master)](https://github.com/91nunocosta/template-pyproject)

This repository provides a [cookiecutter](https://github.com/cookiecutter/cookiecutter)
for Python projects.
It generates the template repo [91nunocosta/template-pyproject](https://github.com/91nunocosta/template-pyproject).

It provides the following base features:

* [poetry](https://python-poetry.org/) setup.
* [pre-commit](https://pre-commit.com/) configuration for linting with multiple linters
  (see [.pre-commit-config.yaml](./{{cookiecutter.package_name}}/.pre-commit-config.yaml)).
* [tox](https://tox.wiki/en/latest/) configuration.
* [GitHub workflow](https://docs.github.com/en/actions/using-workflows) for testing
  with [tox](https://tox.wiki/en/latest/).

## Usage

To create a new Python project, run the following command, and answer all prompts.

```bash
cookiecutter https@github.com/91nunocosta/cookiecutter-pyproject.git
```

### Extra features

* `cli`: configures command script with [typer](https://typer.tiangolo.com/).
* `opensource`: files for open-source projects (e.g., `LICENSE`, `CONTRIBUTING`, `CODE_OF_CONDUCT`).
* `docs`: configures a
  [GitHub workflow](https://docs.github.com/en/actions/using-workflows/about-workflows)
  for publishing documentation into [GitHub pages](https://pages.github.com/)
* `release`: configures a
  [GitHub workflow](https://docs.github.com/en/actions/using-workflows/about-workflows)
  for publishing the Python package into [pypi](https://pypi.org/).

### Contributing

If you want to contribute, please read the [contributing guidelines](./CONTRIBUTING.md)
and [code of conduct](./CODE_OF_CONDUCT.md).
