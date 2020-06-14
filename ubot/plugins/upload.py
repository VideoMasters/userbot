import os
from pyrogram import Client as uBot , Filters
async def upload(uBot,usr,path,replacer):
    if os.path.isdir(path) :
        p=path.replace(replacer,'')
        await uBot.send_message(usr,p,parse_mode=None)
        print(path)
        Files=os.listdir(path)
        Files.sort()
        for file in Files :
            path=path+"/"+file
            await upload(uBot,usr,path,replacer)
            path= path.replace("/"+file,'')
            if file is Files[-1] :
                p=path.replace(replacer,'')
                print(p)
                await uBot.send_message(usr,p,parse_mode=None)
    else:
        await uBot.send_document(usr,path)
        print(path)

@uBot.on_message(Filters.me & Filters.command('upload','.'))
async def _upload(uBot,message):
    path = message.text.split('.upload ')[1]
    replacer=os.path.dirname(path)+'/'
    usr=message.chat.id
    await upload(uBot,usr,path,replacer)

