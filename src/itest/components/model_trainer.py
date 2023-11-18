from noops.utils.logger import get_logger
from noops.utils.yaml import handle_yaml
from dataclasses import dataclass
import os


logger=get_logger()
yaml_handler=handle_yaml()


@dataclass
class ModelTrainerConfig():

    config=yaml_handler.read_data(
        os.path.join(
            os.getcwd(),
            "src","itest",
            "config","modelbuild.yaml"
            )
        )


class ModelTrainer():

    def __init__(self) -> None:
        self.config=ModelTrainerConfig().config
