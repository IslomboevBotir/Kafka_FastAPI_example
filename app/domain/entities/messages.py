from dataclasses import field, dataclass

from app.domain.values.messages import Text
from app.domain.values.messages import Title
from app.domain.entities.base import BaseEntity
from app.domain.events.messages import NewMessageReceivedEvent


@dataclass(eq=False, frozen=True)
class Message(BaseEntity):
    text: Text


@dataclass(eq=False, frozen=True)
class Chat(BaseEntity):
    title: Title
    messages: set[Message] = field(
        default_factory=set,
        kw_only=True
    )

    def add_message(self, message: Message):
        self.messages.add(message)
        self.register_event(NewMessageReceivedEvent(
            message_text=message.text.as_generic_type(),
            chat_oid=self.oid,
            message_oid=message.oid,
        ))
