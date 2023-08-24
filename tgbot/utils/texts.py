from aiogram.types import Message, User, CallbackQuery


def user_commands_guide() -> str:
    return (
        f'<b>Команды, которые доступны в группе:</b>\n\n'

        f'1. <b>!help</b> или <b>/help</b> - отправляет в диалог с ботом (т.е. в этот чат) основную информацию '
        f'для написания дипломного проекта.\n\n'

        f'2. <b>!report</b> или <b>/report</b> - позволяет вам пожаловаться на какое-то конкретное сообщение '
        f'в учебном чате.\n'
        f'<i>Жалобу нельзя отправить на сообщение от владельца или администратора чата, а также от бота</i>.\n'
        f'<i>При использовании данной команды ваша жалоба вместе со ссылкой на сообщение отправится в личные '
        f'сообщения администраторам группы. Не злоупотребляйте этой функцией.</i>\n'
        f'<b>Данная команда должна вводится в <u>ответе</u> на то сообщение, '
        f'на которое вы хотите пожаловаться.</b>\n\n'

        f'3. <b>!paste</b> или <b>/paste</b> - вставить сообщение с рукописным кодом на hastebin-сервер '
        f'для удобства его чтения. После выполнения команды сообщение с кодом удалится, а взамен бот вышлет вам '
        f'ссылку, по которой будет лежать код в привычном вам виде.\n'
        f'<b>Данная команда должна вводится в <u>ответе</u> на то сообщение, '
        f'которое вы хотите поместить на hastebin-сервер.</b>\n\n'

        f'4. В группе действует система рекомендаций, для того чтобы отблагодарить человека, который вам помог '
        f'достаточно  в ответ на его сообщение написать "Спасибо"'
    )


def user_help_text(message: Message) -> str:
    return (f'Привет, {message.from_user.get_mention()}!'

            f'\n\nСсылка на <b>базовые советы по дипломному проекту:</b>'
            f'<a href="https://magnetic-evergreen-187.notion.site/Python-Basic-3ac614e60b7e434e9d9c018023319c04">'
            f' ТУТ </a>'

            f'\n\nСсылка на <b>видео по подключению к базам данных:</b>'
            f'<a href="https://youtu.be/TCdyfEvrIUg?list=PLA0M1Bcd0w8x4Inr5oYttMK6J47vxgv6J"> перейти в youtube </a>'

            f'\n\nP.S. Итоговая презентация проектов - отменена. '
            f'Вместо неё только защита дипломного проекта перед куратором.\n'
            f'Вы можете посмотреть записи прошедших презентаций по'
            f'<a href="https://docs.google.com/spreadsheets/d/1KbM7aPC4iYcNqm89nUNlQkplxQdfFGYdT2whYgF4V38/edit#gid=0">'
            f' ссылке </a>')


def admin_help_text(message: Message) -> str:
    return (
        f'Привет, администратор {message.from_user.get_mention()}!'
        f'\n\n<b>Список доступных команд:</b>'
        f'\n<i>Обе команды необходимо вводить в ответ на пересылаемое сообщение от пользователя, '
        f'к которому хотите применить команду.\n'
        f'Обе команды нельзя применить ни к владельцу чата, ни к администраторам чата.</i>'

        f'\n\n1. <b>!b или !ban</b> &lt;<i>причина бана</i>&gt; - Забанить пользователя c указанием причины. '
        f'\n<i>Всё, что будет написано через 1 пробел после команды - будет указано в инфо-сообщении</i>'

        f'\n\n2. <b>!ro</b> &lt;<i>число</i>&gt;&lt;<i>время</i>&gt; - Активировать режим "только чтение" '
        f'для пользователя.'
        f'\n<u>число</u> - число на которое выдает РО, '
        f'\n<u>время</u> - буквенное обозначение периода (m - минуты, h - часы, d - дни, w - недели).'
        f'\n<i>В случае, если команда передана без аргументов, то режим "только чтение" будет установлен '
        f'по умолчанию на 15 минут.</i>\n'

        f'\n\n3. <b>!toprep</b> - Выводит рейтинг пользователей'
    )


def greeting_text(call: CallbackQuery, bot_user: User) -> str:
    return (
        f'Привет, {call.from_user.full_name}!\n\n'
        f'\n\n<b>Для начала ответьте на каптчу</b>\n'
        f'Прежде чем задавать вопросы - прочитай <b>базовые советы по дипломному проекту:</b> '
        f'<a href="https://magnetic-evergreen-187.notion.site/Python-Basic'
        f'-3ac614e60b7e434e9d9c018023319c04"> ТУТ </a> '

        f'\n\nА также ознакомься со всеми <b>закрепленными сообщениями</b> в этом чате.\n\n'

        f'Чтобы узнать, что я могу делать в этом чате - напиши мне @{bot_user.username} команду <i>/start</i> '
        f'в <b>личном сообщении</b>.'
    )
