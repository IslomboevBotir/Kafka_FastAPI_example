from app.infra.repositories.messages import MemoryChatRepository, BaseChatRepository
from app.logic.mediator import Mediator
from app.logic.commands.messages import CreateChatCommand, CreateChatCommandHandler


def init_mediator(
        mediator: Mediator,
        chat_repository: BaseChatRepository,
):
    mediator.register_command(
        CreateChatCommand,
        [CreateChatCommandHandler(chat_repository=chat_repository)],
    )

