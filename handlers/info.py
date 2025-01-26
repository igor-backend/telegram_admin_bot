from aiogram import Router, html
from aiogram.filters import Command
from aiogram.types import Message


info_router = Router()


@info_router.message(Command('chat_info'))
async def command_chat_info_handler(message: Message) -> None:
    text = (f'{html.bold("Chat name")}: {html.code(message.chat.full_name)}\n'
            f'{html.bold("Chat ID")}: {html.code(message.chat.id)}\n'
            f'{html.bold("Thread ID")}: {html.code(message.message_thread_id or "-")}\n'
            f'{html.bold("Chat type")}: {html.code(message.chat.type)}')
    await message.answer(text)
