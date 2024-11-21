from dataclasses import dataclass

from app.logic.exceptions.base import LogicException


@dataclass(eq=False)
class EventHandlersNotRegisteredException(LogicException):
    event_type: type

    @property
    def message(self):
        return f"You have not registered any handlers{self.event_type}"


@dataclass(eq=False)
class CommandHandlersNotRegisteredException(LogicException):
    command_type: type

    @property
    def message(self):
        return f"Don`t find handler for commands: {self.command_type}"
