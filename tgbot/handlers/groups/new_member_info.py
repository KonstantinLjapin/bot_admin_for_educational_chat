from aiogram import Dispatcher
from aiogram.types import Message


async def new_member_info(message: Message) -> None:
    """ Хендлер для приветствия нового пользователя группы с полезными ссылками. """

    # текст приветствия нового пользователя с поелзными ссылками
    greeting: str = \
        (f'Привет, {message.new_chat_members[0].first_name}!\n\n'
         f'Прежде чем задавать вопросы - прочитай <b>базовые советы по дипломному проекту:</b> '
         f'<a href="https://magnetic-evergreen-187.notion.site/Python-Basic-3ac614e60b7e434e9d9c018023319c04"> ТУТ </a>'
         f'\n\nА также ознакомься со всеми <b>закрепленными сообщениями</b> в этом чате.\n\n'
         f'Если понадобиться моя помощь - напиши мне в ЛС @EducationalChatAdmin_bot команду <i>!help</i>')

    await message.answer(text=greeting, disable_web_page_preview=True)


def register_new_member_info(dp: Dispatcher):
    dp.register_message_handler(new_member_info, content_types=['NEW_CHAT_MEMBERS'])