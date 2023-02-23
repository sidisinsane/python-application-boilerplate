# Python Application Boilerplate

 

## Getting Started

This boilerplate uses [Pipenv](https://pipenv.pypa.io/en/latest/) to manage dependencies and its virtual environment. You will need to install it if you do not already have it.



### 1. Install Project Dependencies

Use Pipenv to create a virtual environment and install the dependencies set in the `Pipfile`. Setting the `--dev` flag will include the *(optional)* development dependencies.

```bash
pipenv install --dev
```

 

### 2. Run Stuff, Do Stuff...



#### Understanding Pipenv Scripts

Scripts set within the `Pipefile` provide a convinient way to run shell commands. They allow you to define shortcuts for commonly-used commands, regardless of whether they need to be executed within a virtual environment or not. To run a script, you simply prefix it with `pipenv run`.



If this in your `Pipefile` *(Look, it is!)*

```
[scripts]
start = "pipenv run python -m my_app --text '1. Check it out!'"
clean = "rm -rf docs && rm -rf reports"
```

Then

- `pipenv run start` executes the command `python -m my_app --text '1. Check it out!'` <u>within</u> the virtual environment 

- `pipenv run clean` executes the simple shell command `rm -rf docs && rm -rf reports` which doesn't require any virtual environment



## Tooling



### Installation and Package Management with [Pipenv](https://pipenv.pypa.io/en/latest/)

**Pipenv** – A production-ready tool that aims to bring the best of all packaging worlds to the Python world. It harnesses Pipfile, pip, and virtualenv into one single command.

Install `pipenv`:

```bash
pip install --user pipenv
```

 

### Linting with [PyLint](https://pylint.readthedocs.io/en/latest/) and [Black](https://black.readthedocs.io/en/stable/index.html)

**Pylint** – Analyses your code without actually running it. It checks for errors, enforces a coding standard, looks for [code smells](https://martinfowler.com/bliki/CodeSmell.html), and can make suggestions about how the code could be refactored.

Install `pylint`:

```bash
pipenv install -d pylint
```

**Black** – Cedes control over minutiae of hand-formatting.

Install`black`:

```bash
pipenv install -d black
```

 

### Testing and Coverage with [Pytest](https://docs.pytest.org/) and [Pytest-cov](https://pypi.org/project/pytest-cov/)

**Pytest** – Framework that makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

Install `pytest`:

```bash
pipenv install -d pytest
```

**Pytest-cov** – Pytest plugin for measuring coverage.

Install `pytest-cov`:

```bash
pipenv install -d pytest-cov
```

 

### Documentation with [Pdoc3](https://pypi.org/project/pdoc3/)

**Pdoc3** – Auto-generate API documentation for Python projects.

Install `pdoc3`:

```bash
pipenv install -d pdoc3
```



### Command-Line Argument Parsing with [Argparse](https://docs.python.org/3/library/argparse.html)

**Argparse** – Parser for command-line options, arguments and sub-commands.

Install `argparse`:

```bash
pipenv install argparse
```
