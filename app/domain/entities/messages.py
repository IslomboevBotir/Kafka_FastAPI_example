from dataclasses import dataclass
from dataclasses import field

from app.domain.values.messages import Text
from app.domain.values.messages import Title
from app.domain.entities.base import BaseEntity


@dataclass(frozen=True)
class Message(BaseEntity):
    text: Text


@dataclass(frozen=True)
class Chat(BaseEntity):
    title: Title
    messages: set[Message] = field(
        default_factory=set,
        kw_only=True
    )

    def add_message(self, message: Message):
        self.messages.add(message)
