# Cookiecuter for Python projects

This repository provides a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template
for python projects.

## Usage

To create a new Python project, run the following command, and answer all prompts.

```bash
cookiecutter https@github.com/91nunocosta/python-package-cookiecutter.git
```

## Project types

The repository provides the following project types.

### Python API library

The Python API library template provides the following:

* [poetry](https://python-poetry.org/) setup
* [pre-commit](https://pre-commit.com/) configuration for linting with multiple linters
  (see [.pre-commit-config.yaml](./{{cookiecutter.package_name}}/.pre-commit-config.yaml))
* [tox](https://tox.wiki/en/latest/) configuration
* [GitHub workflows](https://docs.github.com/en/actions/using-workflows) for:
  * lint commit messages according to [Conventional Commit](https://www.conventionalcommits.org/en/v1.0.0/)
  * test with _tox_
  * release the package with [Python Semantic Release](https://python-semantic-release.readthedocs.io/en/latest/)

### Contributing

If you want to contribute, please read the [contributing guidelines](./CONTRIBUTING.md)
and [code of conduct](./CODE_OF_CONDUCT.md).
