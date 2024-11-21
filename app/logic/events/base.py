from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from typing import TypeVar
from typing import Generic
from typing import Any

from app.domain.events.base import BaseEvent

ET = TypeVar('ET', bound=BaseEvent)
ER = TypeVar('ER', bound=Any)


@dataclass
class EventHandler(ABC, Generic[ET, ER]):
    @abstractmethod
    def handle(self, event: ET) -> ER:
        ...
