from dataclasses import dataclass

from app.domain.values.base import BaseValueObject
from app.domain.exceptions.messages import TitleTooLongException
from app.domain.exceptions.messages import EmptyTextException


@dataclass(frozen=True)
class Text(BaseValueObject):
    value: str

    def validate(self):
        if not self.value:
            raise EmptyTextException()

    def as_generic_type(self):
        return str(self.value)


@dataclass(frozen=True)
class Title(BaseValueObject):
    value: str

    def validate(self):
        if not self.value:
            raise EmptyTextException()
        if len(self.value) > 255:
            raise TitleTooLongException(self.value)

    def as_generic_type(self):
        return str(self.value)
