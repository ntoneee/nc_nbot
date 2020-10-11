import logging
from telethon import TelegramClient
from telethon.tl.custom import Button
from telethon.events import InlineQuery, CallbackQuery
import config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(msg)s', level=logging.INFO)
bot = TelegramClient('bot', config.api_id, config.api_hash)


@bot.on(InlineQuery())
async def inline(event: InlineQuery.Event):
    builder = event.builder
    await event.answer([
        builder.article(
            title='Текст без комментариев',
            description=event.text,
            text=event.text,
            buttons=Button.inline('Комментарии отключены')
        )
    ])


@bot.on(CallbackQuery())
async def callback(event: CallbackQuery.Event):
    await event.answer()


if __name__ == '__main__':
    logging.info("Staring bot!")
    bot.start(bot_token=config.token)
    bot.run_until_disconnected()
