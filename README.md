# Python UV Asessment

[![ci.yml](https://github.com/elastic/mvp-mlops-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/elastic/mvp-mlops-platform/actions/workflows/ci.yml)
[![publish.yml](https://github.com/avillalba-elastic/python-uv-asessment/actions/workflows/publish.yml/badge.svg)](https://github.com/avillalba-elastic/python-uv-asessment/actions/workflows/publish.yml)
[![Documentation](https://img.shields.io/badge/documentation-available-brightgreen.svg)](https://avillalba-elastic.github.io/python-uv-asessment/)
[![License](https://img.shields.io/github/license/avillalba-elastic/python-uv-asessment)](https://github.com/avillalba-elastic/python-uv-asessment/blob/main/LICENCE.txt)
[![Release](https://img.shields.io/github/v/release/avillalba-elastic/python-uv-asessment)](https://github.com/avillalba-elastic/python-uv-asessment/releases)

Assessment of the new [uv tool](https://docs.astral.sh/uv/) to manage Python packages and projects. 

Inspired by [this post in the MLOps Community](https://home.mlops.community/home/blogs/poetry-was-good-uv-is-better-an-mlops-migration-story-2025-02-03?utm_campaign=Weekly+Newsletter+-+2025-02-06&utm_content=Weekly+Newsletter&utm_medium=KQcFSzsMJAUFCS8ECAwIBD4RIQpKBiI&utm_source=customer.io).

# Installation

We use the package manager [Poetry](https://python-poetry.org/). Follow [these instructions](https://python-poetry.org/docs/#installation) to install it.

Install the virtual environment:
```bash
poetry install
```

Install [pre-commit hooks](https://pre-commit.com/):

```bash
poetry run invoke installs.pre-commit
```

# Tests

We use [pytest](https://docs.pytest.org/en/stable/) and [nox](https://nox.thea.codes/en/stable/) to run the tests:

To run the tests with the default Python and dependency versions:

```bash
poetry run invoke testing.test-default-versions
```

To run the tests with the dependency versions matrix:

```bash
poetry run invoke testing.test-matrix-versions
```

# Relevant links
- [SonarQube project](https://sonar.elastic.dev/tutorials?id=)