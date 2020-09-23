from pyrogram import Client , Filters
from youtube_dl import YoutubeDL
ytdl=YoutubeDL()
@Client.on_message((Filters.me | Filters.outgoing ) & Filters.command('ytdl','.'))
async def ytdl_f(uBot,message):
    if '|' in message.text:
        texts=message.text.split('|')
        link=texts[0].split()[1]
        f=texts[1]
        info=ytdl.extract_info(link,download=False)
        title=info['title']
        ext=[format['ext'] for format in  info['formats'] if int(format['format_id'])==int(f)][0]
        
        print(title+'.'+ext)
        #ytdl.download(link)
    else:
        link=message.text.split()[1]
        formats=ytdl.extract_info(link,download=False)['formats']
        options=''
        for format in formats:
            size=format['filesize']
            if size is None:
                size=''
            else :
                size=str(round(size/(1024*1024),2))+'MB'
            option=format['format_id']+' '+format['ext']+' '+format['format_note']+' '+size+'\n'
            options+=option
        await message.reply(options)
        

