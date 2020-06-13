import asyncio
from pyrogram import Client as uBot , Filters
@uBot.on_message(Filters.me & Filters.command('exec','.'))
async def _(uBot,message):
    
    cmd = message.text.split('.exec ')[1]
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    e = stderr.decode()
    if not e:
        e = "No Error."
    o = stdout.decode()
    if not o:
        o = "No Output.`"
    OUTPUT = f"**QUERY:**\n__Command:__\n`{cmd}` \n__PID:__\n`{process.pid}`\n\n**stderr:** \n`{e}`\n**Output:**\n{o}"
    await uBot.send_message(message.chat.id,OUTPUT)
    print(message)
