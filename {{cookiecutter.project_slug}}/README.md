# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}


## Prerequisites

This project use `python{{ cookiecutter.python_version }}` and
`aiohttp` to work and `tox` to be linted.

Dev requirements are in `requirements-dev.txt`.


## Contributing

To run the server locally, you can use `adev`:

```bash
$ adev runserver {{ cookiecutter.project_slug }}/{{ cookiecutter.project_slug }}.py
```

If you need to add a dev requirement, add it in the
`requirements-dev.in` file, and run `pip-compile requirements-dev.in`
(`pip-compile` is from the `pip-tools` package).

After commiting something, run `tox -p auto` to check your code and
run the tests.


## Running

To run the application, simply execute `{{ cookiecutter.project_slug }}` under the folder with the same name:

```bash
$ python{{ cookiecutter.python_version }} {{ cookiecutter.project_slug }}
```
