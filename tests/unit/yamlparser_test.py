import dataclasses
import pytest

from yamlparser.yamlparser import YamlParser, YamlParserException
from tests.unit.simple_dataclass import SimpleDataclass, SimpleDataclassException
from tests.conftest import TEST_ROOT_DIR


def test_invalid_filepath():

    filepath = "./resources/file.yaml"
    model = SimpleDataclass

    with pytest.raises(YamlParserException) as exception:
        YamlParser(
            filepath=filepath,
            model=model
        )

    assert str(exception.value) == f"{filepath} is not a valid filepath"


def test_model_not_dataclass():

    filepath = f"{TEST_ROOT_DIR}/resources/valid.yaml"
    model = "Not a dataclass type"

    with pytest.raises(YamlParserException) as exception:
        YamlParser(
            filepath=filepath,
            model=model
        )

    assert str(exception.value) == f"model expects a 'dataclass' type, but input has type: <class 'str'>"


def test_read_valid_yaml():

    yaml_parser = YamlParser(
        filepath=f"{TEST_ROOT_DIR}/resources/valid.yaml",
        model=SimpleDataclass
    )

    actual_dataclass = yaml_parser.read()

    expected_dictionary = {
        "application_name": "Test",
        "memory": 2.5,
        "workers": 1,
        "log_level": "INFO",
        "dynamic_scaling": False,
        "system_variables": {}
    }

    assert dataclasses.asdict(actual_dataclass) == expected_dictionary


def test_read_invalid_yaml():

    yaml_parser = YamlParser(
        filepath=f"{TEST_ROOT_DIR}/resources/invalid.yaml",
        model=SimpleDataclass
    )

    with pytest.raises(SimpleDataclassException) as exception:
        yaml_parser.read()

    assert str(exception.value) == f"memory expects a 'float' type, but input has type: <class 'str'>"
