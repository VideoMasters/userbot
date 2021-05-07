from pyrogram import Client, filters

ALIVE = 'I am ALIVE sir .'


@Client.on_message((filters.me | filters.outgoing) & filters.command('alive', '.'))
async def _alive(uBot, message):
    await message.edit(ALIVE)


@Client.on_message(filters.private & ~ filters.me & ~ filters.bot & (filters.regex(r'(?i)\b(hello|hi|hii|hiii|hye|hy)\b')))
async def _hello(uBot, message):
    await message.reply('Hello {}.'.format(message.from_user.first_name))


@Client.on_message(~ filters.me & filters.command('ualive', '.'))
async def _ualive(uBot, message):
    reply = await message.reply('.alive')
    await _alive(uBot, reply)


@Client.on_message(filters.private & ~ filters.me & ~ filters.bot & (filters.regex(r'(?i)\b(thanks|thnks|thnx|thnk|thank)\b')))
async def _thank(uBot, message):
    await message.reply('You welcome {}'.format(message.from_user.first_name))


@Client.on_message(filters.private & ~ filters.me & ~ filters.bot & (filters.regex(r'(?i)(How are (you|u))')))
async def reply_fine(uBot, message):
    await message.reply('I am fine.\nWhat about you, {}?'.format(message.from_user.first_name))
