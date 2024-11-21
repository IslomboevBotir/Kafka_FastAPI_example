from dataclasses import dataclass

from app.domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class LogicException(ApplicationException):
    @property
    def message(self):
        return "an error occurred while processing"
