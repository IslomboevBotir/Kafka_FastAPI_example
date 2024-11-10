from dataclasses import dataclass
from typing import Generic
from typing import TypeVar
from typing import Any
from abc import ABC, abstractmethod

VT = TypeVar('VT', bound=Any)


@dataclass(frozen=True)
class BaseValueObject(ABC, Generic[VT]):
    value: VT

    def __post_init__(self):
        self.validate()

    @abstractmethod
    def validate(self):
        ...

    @abstractmethod
    def as_generic_type(self):
        ...