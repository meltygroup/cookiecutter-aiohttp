# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Prerequisites

This project use `python{{ cookiecutter.python_version }}` and `aiohttp` to work and `detox` to be linted.

## Building

By running `detox` you will:
* Validate the coding style (thanks to a lot of linters)
{% if cookiecutter.has_docs == "y" %}
* Build the docs using sphinx
{% endif %}

```bash
$ detox
```

## Running

To run the application, simply execute `{{ cookiecutter.project_slug }}` under the folder with the same name:

```bash
$ python{{ cookiecutter.python_version }} {{ cookiecutter.project_slug }}
```
