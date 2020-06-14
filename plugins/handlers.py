from pyrogram import Client as uBot , Filters
ALIVE = 'I am ALIVE sir .'
@uBot.on_message(Filters.me & Filters.command('alive','.'))
async def _alive(uBot,message):
    await message.edit(ALIVE)    
@uBot.on_message(Filters.private & ~ Filters.me & ~ Filters.bot & (Filters.regex(r'(?i)\b(hello|hi|hii|hiii|hye|hy)\b')))
async def _hello(uBot,message):
   await  message.reply('Hello {}'.format(message.from_user.first_name))
@uBot.on_message( ~ Filters.me & Filters.command('ualive','.'))
async def _ualive(uBot,message):
    reply=await message.reply('.alive')
    await _alive(uBot,reply)
@uBot.on_message(Filters.private & ~ Filters.me & ~ Filters.bot  & (Filters.regex(r'(?i)\b(thanks|thnks|thnx|thnk|thank)\b')))
async def _thank(uBot,message):
    await message.reply('You welcome {}'.format(message.from_user.first_name))
@uBot.on_message(Filters.private & ~ Filters.me & ~ Filters.bot  & (Filters.regex(r'(?i)(How are (you|u))')))
async def reply_fine(uBot,message):
    await message.reply('I am fine.\nWhat about you, {}?'.format(message.from_user.first_name))
