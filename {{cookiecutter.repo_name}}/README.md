{{cookiecutter.repo_name}}
=========================

## Development

Follow the instructions below to setup the repository locally.

After moving to the repository, create the virtualenv:

```
$ virtualenv env
```

Activate the virtualenv and install the requirements:

```
$ env/Scripts/activate
$ pip install -r requirements.txt
```

Additionally, it is recommended you install the development requirements:
```
$ pip install -r requirements-dev.txt
```

Setup the package links for development:

```
$ python setup.py develop
```

### pre-commit

In order to use the [pre-commit](https://pre-commit.com/) strategy, simply run the following after having installed the requirements.

```
$ pre-commit install
```

When using pre-commit, it is recommended to use Visual Studio Code with format on save targeting [black](https://github.com/psf/black).

## Documentation

If you already installed the requirements, in order to see the documentation, simply launch the local web server:

```
$ mkdocs serve
```
