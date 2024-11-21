from dataclasses import dataclass

from app.logic.exceptions.base import LogicException


@dataclass(eq=False)
class ChatWithThatTitleAlreadyExistsException(LogicException):
    title: str

    @property
    def message(self):
        return f"Chat with title {self.title} already exists"
