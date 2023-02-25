"""
обработка команды /start
"""

from telethon import events, Button

# кнопки команд
button_main_cmd = [
    [Button.text("/help")]
]


@tlgbot.on(events.NewMessage(chats=tlgbot.settings.get_all_user_id(), pattern='/start'))
async def start_cmd_plugin(event):
    await event.respond("Привет! жми на команды и получай получай информацию!", buttons=button_main_cmd)
