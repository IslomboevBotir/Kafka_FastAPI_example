from abc import ABC
from uuid import uuid4
from dataclasses import dataclass
from dataclasses import field
from copy import copy
from datetime import datetime

from app.domain.events.base import BaseEvent


@dataclass(eq=False, frozen=True)
class BaseEntity(ABC):
    oid: str = field(
        default_factory=lambda: str(uuid4()),
        kw_only=True
    )
    _events: list[BaseEvent] = field(
        default_factory=list,
        kw_only=True
    )
    created_at: datetime = field(
        default_factory=lambda: datetime.now(),
        kw_only=True
    )

    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, __value: 'BaseEntity') -> bool:
        return self.oid == __value.oid

    def pull_event(self) -> list[BaseEvent]:
        registered_events = copy(self._events)
        self._events.clear()
        return registered_events

    def register_event(self, event: BaseEvent) -> None:
        self._events.append(event)
