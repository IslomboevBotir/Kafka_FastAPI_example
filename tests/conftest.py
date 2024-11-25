from pytest import fixture

from app.infra.repositories.messages import BaseChatRepository, MemoryChatRepository
from app.logic.mediator import Mediator
from app.logic.init import init_mediator


@fixture(scope='function')
def chat_repository() -> MemoryChatRepository:
    return MemoryChatRepository()


@fixture(scope='function')
def mediator(
        chat_repository: BaseChatRepository,
) -> Mediator:
    mediator = Mediator()
    init_mediator(mediator=mediator, chat_repository=chat_repository)
    return mediator
