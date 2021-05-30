# pyyaml-parser

Library that wraps the `PyYAML` library and enables validation of ingested YAML files.  The project is used in conjunction
with other repositories to demonstrate the use of shared libraries via a private PyPi repository: 

* https://github.com/alanb-2/k8s-sonatype-nexus
* https://github.com/alanb-2/python-import-library

## Prerequisites

* `python 3.9.5`
* `poetry 1.1.6`

Note: the instructions assume that the artifact repository in https://github.com/alanb-2/k8s-sonatype-nexus is up and running,
the admin user has been initialised and that the necessary PyPi repositories have been created.

### Poetry

1.  Install `poetry`: 
    ```shell
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - 
    ```
    Note: this command will make use of the path that `python` is linked to.  `pyenv` is the recommended tool to manage
    the `python` environment that `poetry` is built against, although building it in a virtual environment will also work.
    
2.  Check that `poetry` is on the `PATH` by executing:
    ```shell
    poetry --version
    ```

3.  Configure the repository endpoints for read and write respectively:
    ```shell
    poetry config repositories.nexus http://localhost:30081/repository/pypi-group/simple
    poetry config repositories.private http://localhost:30081/repository/pypi-private/
    ```

4.  Store the repository configurations:
    ```shell
    poetry config http-basic.nexus $USERNAME
    poetry config http-basic.private $USERNAME
    ```
    where the default Nexus repository `USERNAME` is `admin`.

5.  Set the `poetry` environment and install the project dependencies:
    ```shell
    poetry env use 3.9.5
    poetry install
    ```

### PyCharm

1.  Install the Poetry plugin for PyCharm (https://plugins.jetbrains.com/plugin/14307-poetry) and restart PyCharm

2.  Goto `File -> Settings` in the menu ribbon and then `Project: <> -> Python Interpreter` in the pane that appears.

3.  Click on the cog in the top-right-hand corner and then `Add` to bring up the `Add Python Interpreter` pane.

4.  Click on the `Poetry Environment` option on the left-hand side and add the `poetry` virtual environment already created.
    This can be found from the CLI by executing:
    ```shell
    poetry env info
    ```
    
5.  Click on `Ok` to complete the configuration and close the pane to return to the `Settings` pane.
    
6.  In the `Settings` pane, click on `Apply` followed by `Ok` to finish configuring the IDE interpreter and close the pane.

## Update dependencies

```shell
poetry update
```

## Test

```shell
poetry run pytest
```

## Test with coverage

```shell
poetry run pytest --cov src/
```

## Build

```shell
poetry build
```

## Publish

Note: the library should be built before running this step.

```shell
poetry publish --repository private
```

## Usage

The `YamlParser` can be defined by supplying an input filepath and dataclass model:

```shell
from yamlparser.yamlparser import YamlParser

yamlparser = YamlParser("./input.yaml", DataclassModel)
```

When `read` is executed, the yaml file will be parsed and the populated dataclass model returned:

```shell
config = yamlparser.read()
```

Since a dataclass is being used to parse the ingested yaml, any validation rules or other logic implemented within the
dataclass initialisation classes will also be executed before returning the dataclass model.
