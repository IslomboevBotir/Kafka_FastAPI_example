from dataclasses import field, dataclass

from app.domain.values.messages import Text
from app.domain.values.messages import Title
from app.domain.entities.base import BaseEntity
from app.domain.events.messages import NewMessageReceivedEvent, NewChatCreated


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

    @classmethod
    def create_chat(cls, title: Title) -> 'Chat':
        new_chat = cls(title=title)
        new_chat.register_event(NewChatCreated(chat_oid=new_chat.oid, chat_title=new_chat.title.as_generic_type()))
        return new_chat

    def add_message(self, message: Message):
        self.messages.add(message)
        self.register_event(NewMessageReceivedEvent(
            message_text=message.text.as_generic_type(),
            chat_oid=self.oid,
            message_oid=message.oid,
        ))
