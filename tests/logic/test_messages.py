import pytest

from faker import Faker

from app.domain.entities.messages import Chat
from app.domain.values.messages import Title
from app.infra.repositories.messages import BaseChatRepository
from app.logic.commands.messages import CreateChatCommand
from app.logic.exceptions.messages import ChatWithThatTitleAlreadyExistsException
from app.logic.mediator import Mediator


@pytest.mark.asyncio
async def test_create_chat_command_success(
        chat_repository: BaseChatRepository,
        mediator: Mediator,
        faker: Faker
):
    # TODO: Should use faker for generate random text
    chat: Chat = (await mediator.handle_command(CreateChatCommand(title=faker.text())))[0]
    assert await chat_repository.check_chat_exists_by_title(title=chat.title.as_generic_type())


@pytest.mark.asyncio
async def test_create_chat_command_title_already_exists(
        chat_repository: BaseChatRepository,
        mediator: Mediator,
        faker: Faker
):
    # TODO: Should use faker for generate random text
    title_text = faker.text()
    chat = Chat(title=Title(title_text))
    await chat_repository.add_chat(chat)
    with pytest.raises(ChatWithThatTitleAlreadyExistsException):
        await mediator.handle_command(CreateChatCommand(title=title_text))

    assert len(chat_repository._save_chats) == 1
