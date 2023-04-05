# {{ cookiecutter.project_name }}
{% if cookiecutter.opensource == "yes" %}
[![Cookiecutter](https://img.shields.io/badge/built%20with-Cookiecutter-ff69b4.svg?logo=cookiecutter)](https://github.com/91nunocosta/cookiecutter-pyproject/releases/tag/v0.11.0)

[![GitHub](https://img.shields.io/github/license/{{ cookiecutter.github_user }}/{{ cookiecutter.package_name }})](https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.package_name }}/blob/master/LICENSE)

![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)

[![Codacy](https://app.codacy.com/project/badge/Grade/cb92f3f137454fae8697c7a6e7334f74)](https://www.codacy.com/gh/{{ cookiecutter.github_user }}/{{ cookiecutter.package_name }}/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content={{ cookiecutter.github_user }}/{{ cookiecutter.package_name }}&amp;utm_campaign=Badge_Grade)

[![Codacy coverage](https://app.codacy.com/project/badge/Coverage/cb92f3f137454fae8697c7a6e7334f74)](https://www.codacy.com/gh/{{ cookiecutter.github_user }}/{{ cookiecutter.package_name }}/dashboard?utm_source=github.com&utm_medium=referral&utm_content={{ cookiecutter.github_user }}/{{ cookiecutter.package_name }}&utm_campaign=Badge_Coverage)

[![GitHub branch checks state](https://img.shields.io/github/checks-status/{{ cookiecutter.github_user }}/{{ cookiecutter.package_name }}/master)](https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.package_name }})

[![Python versions](https://img.shields.io/pypi/v/{{ cookiecutter.package_name }})](https://pypi.org/project/{{ cookiecutter.package_name }}/)

[![PyPI version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.package_name }})](https://pypi.org/project/{{ cookiecutter.package_name }}/)
{% endif %}
{{ cookiecutter. project_description }}

## Installation

```bash
pip install {{ cookiecutter.package_name }}
```

## Usage

```python
>>> from {{ cookiecutter.module_name }} import fib
>>> fib(0)
0

```

For more details, read the
[documentation](https://{{ cookiecutter.github_user }}.github.io/{{ cookiecutter.package_name }}/{{ cookiecutter.module_name }}.html).
{% if cookiecutter.opensource == "yes" %}
## Contributing

If you want to contribute, please read the [contributing guidelines](./CONTRIBUTING.md)
and [code of conduct](./CODE_OF_CONDUCT.md).
{% else %}
## Development

### Preparing the development environment

If you want to test or change the source code, prepare your local environment.

1. Clone the repository.

   ```bash
   git clone git@github.com:{{ cookiecutter.github_user }}/{{ cookiecutter.package_name }}.git
   ```

2. Open the project directory.

   ```bash
   cd {{ cookiecutter.package_name }}
   ```

3. Install [_poetry_](https://python-poetry.org/) _package and dependency manager_.
Follow the [poetry installation guide](https://python-poetry.org/docs/#installation).
Chose the method that is more convenient to you, for example:

   ```bash
   curl -sSL\
        https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py \
      | python -
   ```

4. Create a new virtual environment (managed by _poetry_) with the project dependencies.

   ```bash
   poetry install --with dev
   ```

5. Enter the virtual environment.

   ```bash
   poetry shell
   ```

6. Install pre-commit verifications.

   ```bash
   pre-commit install -t pre-commit -t pre-push -t commit-msg
   ```

### Pre-commit

Pre-commit runs the linters and tests configured in
[.pre-commit-config.yaml](./.pre-commit-config.yaml).
You can check the _pre-commit_ phase locally:

1. Prepare the development environment, as described in
[**Preparing the development environment**](#preparing-the-development-environment).

2. Run pre-commit with all files.

```bash
pre-commit run --all-files
```

### Tests

Tests are executed by [tox.ini](./tox.ini).
You can check the _tox_ phase locally:

1. Prepare the development environment, as described in
[**Preparing the development environment**](#preparing-the-development-environment).

2. Run tox.

```bash
tox
```
{% endif -%}
