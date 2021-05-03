from dataclasses import dataclass, field
from typing import Optional


class SimpleDataclassException(Exception):
    pass


@dataclass
class SimpleDataclass:

    application_name: str
    memory: float
    workers: int
    log_level: str
    dynamic_scaling: bool = False
    system_variables: dict = field(default_factory=dict)

    def __post_init__(self):
        error_message = self._validate_init()

        if error_message:
            raise SimpleDataclassException(error_message)

    def _validate_init(self) -> Optional[str]:

        log_levels = ["INFO", "DEBUG", "WARN", "ERROR"]

        error_messages = []

        if not isinstance(self.application_name, str):
            error_messages.append(f"application_name expects a 'str' type, but input has type: {type(self.application_name)}")

        if not isinstance(self.memory, float):
            error_messages.append(f"memory expects a 'float' type, but input has type: {type(self.application_name)}")

        if not isinstance(self.workers, int):
            error_messages.append(f"workers expects an 'int' type, but input has type: {type(self.application_name)}")

        if self.log_level not in log_levels:
            error_messages.append(f"log_level={self.log_level} is not a valid log level ({log_levels})")

        if not isinstance(self.dynamic_scaling, bool):
            error_messages.append(f"dynamic_scaling expects a 'bool' type, but input has type: {type(self.dynamic_scaling)}")

        if self.dynamic_scaling is True and "-DmaxWorkers" not in self.system_variables:
            error_messages.append(f"dynamic_scaling=True, -DmaxWorkers must be defined in system_variables")

        if error_messages:
            return "; ".join(error_messages)
        else:
            return None
