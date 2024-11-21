from dataclasses import dataclass
from dataclasses import field
from abc import ABC
from abc import abstractmethod

from app.domain.entities.messages import Chat


@dataclass
class BaseChatRepository(ABC):
    @abstractmethod
    async def check_chat_exists_by_title(self, title: str) -> bool:
        ...

    @abstractmethod
    async def add_chat(self, chat: Chat) -> None:
        ...


@dataclass
class MemoryChatRepository(ABC):
    _save_chats: list[Chat] = field(
        default_factory=list,
        kw_only=True
    )

    async def check_chat_exists_by_title(self, title: str) -> bool:
        try:
            return bool(
                next(chat for chat in self._save_chats if chat.title.as_generic_type() == title)
            )
        except StopIteration:
            return False

    async def add_chat(self, chat: Chat) -> None:
        self._save_chats.append(chat)
