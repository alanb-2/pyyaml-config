# pyyaml-config

Library that wraps the `PyYAML` library and enables validation of ingested YAML files.

## Prerequisites

* `python 3.9`
* `poetry 1.1.6`

### Poetry

This project makes use of `poetry` to manage the build.  

1.  Install `poetry`: 
    ```shell
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - 
    ```
    Note: this command will make use of the path that `python` is linked to.  It's recommended to create and activate a 
    virtual environment for the installation so that `poetry` is decoupled from any system versions of `python`.
    
2.  Check that `poetry` is on the `PATH` by executing:
    ```shell
    poetry --version
    ```
    Note: if this command doesn't work manually add the `poetry` bin directory to the `PATH`.  The output of step 1
    will indicate where `.poetry/bin` exists.
    
3.  Install the project dependencies:
    ```shell
    poetry install
    ```

### PyCharm

Follow these instructions if `poetry` was installed in a virtual environment.

1.  Install the Poetry plugin for PyCharm (https://plugins.jetbrains.com/plugin/14307-poetry) and close PyCharm
2.  Open a terminal and activate the virtual environment that contains `poetry` e.g.
    ```shell
    conda activate python3.9
    ```
3.  In the same terminal, open PyCharm e.g.
    ```shell
    pycharm-community
    ```
4.  Goto `File -> Settings` in the menu ribbon and then `Project: <> -> Python Interpreter` in the pane that appears.
5.  Click on the cog in the top-right-hand corner and then `Add` to bring up the `Add Python Interpreter` pane.
6.  Click on the `Poetry Environment` option on the left-hand side and create a new `poetry` environment by pointing to the virtual environment `python` binary.
7.  Click on `Ok` to complete the configuration and close the pane to return to the `Settings` pane.
8.  In the `Settings` pane, click on `Ok` and then `Apply` to finish configuring the IDE interpreter.
    
## Commands

### Update dependencies

```shell
poetry update
```

### Test

```shell
poetry run pytest
```

## Resources

Poetry for Python: https://python-poetry.org/docs/
