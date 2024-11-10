from abc import ABC
from uuid import uuid4
from datetime import datetime
from dataclasses import dataclass
from dataclasses import field


@dataclass(eq=False, frozen=True)
class BaseEntity(ABC):
    oid: str = field(
        default_factory=lambda: str(uuid4()),
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
