from dataclasses import dataclass

from app.domain.values.base import BaseValueObject
from app.domain.exceptions.messages import TextTooLongException


@dataclass(frozen=True)
class Text(BaseValueObject):
    value: str

    def validate(self):
        if len(self.value) > 255:
            raise TextTooLongException(self.value)

    def as_generic_type(self):
        return str(self.value)
