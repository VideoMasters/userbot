from pyrogram import Client , Filters
from youtube_dl import YoutubeDL
ytdl=YoutubeDL()
@Client.on_message((Filters.me | Filters.outgoing ) & Filters.command('ytdl','.'))
async def ydl(uBot,message):
    if '|' in message.text:
        texts=message.text.split('|')
        link=texts[0].split()[1]
        f=texts[1]
        info=ytdl.extract_info(link,download=False)
        ytdl.params['format']=f
        if info.get('_title')=='playlist':
            ytdl.params['outtmpl']='%(playlist)s/%(playlist_index)s.%(title)s.%(ext)s'    
        elif info.get('_title')=='channel':
            print('channel')
            pass
        else:
            ytdl.params['outtmpl']='%(title)s.%(ext)s'
        ytdl.download([link])

    else:
        link=message.text.split()[1]
        info=ytdl.extract_info(link,download=False)
        formats=info['formats']
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
        
        

