# uv-dynamic-versioning

[![PyPI version](https://badge.fury.io/py/uv-dynamic-versioning-nopydantic.svg)](https://badge.fury.io/py/uv-dynamic-versioning-nopydantic)

[poetry-dynamic-versioning](https://github.com/mtkennerly/poetry-dynamic-versioning) influenced dynamic versioning tool for [uv](https://github.com/astral-sh/uv)/[hatch](https://github.com/pypa/hatch), powered by [dunamai](https://github.com/mtkennerly/dunamai/).

## Introduction

This fork exists to cut out the pydantic dependency in uv-dynamic-versioning. 

Pydantic Core takes a bit longer to be ready for new Python releases. For example, as of writing, Python 3.14RC1 is out, but Pydantic isn't yet available.

This fork is intended to be a minimal fork that only removes the type checking in the data layer so that adopters can leverage uv-dynamic-versioning without the pydantic dependency. 