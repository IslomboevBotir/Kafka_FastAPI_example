from dataclasses import dataclass

from app.domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class TitleTooLongException(ApplicationException):
    text: str

    @property
    def message(self):
        return f"Very long text message: {self.text}"


@dataclass(eq=False)
class EmptyTextException(ApplicationException):
    def message(self):
        return "Text cannot be empty"
