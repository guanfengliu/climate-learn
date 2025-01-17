# Standard library
from __future__ import annotations
from abc import ABC
import copy
from typing import Any, Callable, Dict, TYPE_CHECKING, Union

# Local application
from climate_learn.data.climate_dataset.args import ClimateDatasetArgs
from climate_learn.data.task.args import TaskArgs

if TYPE_CHECKING:
    from climate_learn.data.dataset import MapDataset


class MapDatasetArgs(ABC):
    _data_class: Union[Callable[..., MapDataset], str] = "MapDataset"

    def __init__(
        self, climate_dataset_args: ClimateDatasetArgs, task_args: TaskArgs
    ) -> None:
        self.climate_dataset_args: ClimateDatasetArgs = climate_dataset_args
        self.task_args: TaskArgs = task_args

    def create_copy(self, args: Dict[str, Any] = {}) -> MapDatasetArgs:
        new_instance: MapDatasetArgs = copy.deepcopy(self)
        for arg in args:
            if arg == "climate_dataset_args":
                new_instance.climate_dataset_args = (
                    new_instance.climate_dataset_args.create_copy(args[arg])
                )
            elif arg == "task_args":
                new_instance.task_args = new_instance.task_args.create_copy(args[arg])
        new_instance.check_validity()
        return new_instance

    def check_validity(self) -> None:
        pass
