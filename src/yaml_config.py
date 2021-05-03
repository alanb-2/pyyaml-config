import os
import yaml

from dataclasses import dataclass, is_dataclass
from typing import Any, Optional


class YamlConfigException(Exception):
    pass


@dataclass
class YamlConfig:

    filepath: str
    model: Any

    def __post_init__(self):

        error_message = self._validate_init()

        if error_message:
            raise YamlConfigException(error_message)

    def _validate_init(self) -> Optional[str]:

        error_messages = []

        if not os.path.isfile(self.filepath):
            error_messages.append(f"{self.filepath} is not a valid filepath")

        if not is_dataclass(self.model):
            error_messages.append(f"model expects a 'dataclass' type, but input has type: {type(self.model)}")

        if error_messages:
            return "; ".join(error_messages)
        else:
            return None

    def read(self) -> Any:

        stream = open(self.filepath, 'r', encoding="utf-8")
        dictionary = yaml.safe_load(stream)

        return self.model(**dictionary)
