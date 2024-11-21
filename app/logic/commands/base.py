from dataclasses import dataclass
from abc import ABC
from abc import abstractmethod
from typing import TypeVar
from typing import Generic
from typing import Any


@dataclass(frozen=True)
class BaseCommand(ABC):
    ...


CT = TypeVar('CT', bound=BaseCommand)
CR = TypeVar('CR', bound=Any)


@dataclass(frozen=True)
class CommandHandler(ABC, Generic[CT, CR]):
    @abstractmethod
    async def handle(self, command: CT) -> CR:
        ...
