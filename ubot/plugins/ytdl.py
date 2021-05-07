import os
import shutil
from io import BytesIO

from pyrogram import Client, filters
from youtube_dl import YoutubeDL

from ubot.plugins import upload

ytdl = YoutubeDL()


@Client.on_message((filters.me | filters.outgoing) & filters.command('ytdl', '.'))
async def ydl(uBot, message):
    if '|' in message.text:
        texts = message.text.split('|')
        link = texts[0].split()[1]
        f = texts[1]
        ytdl.params['format'] = f

        info = ytdl.extract_info(link, download=False)
        if info.get('_type') == 'playlist':
            path = info['title']
            ytdl.params['outtmpl'] = path + \
                '/%(playlist_index)s.%(title)s.%(ext)s'
        else:
            ext = next(format['ext']
                       for format in info['formats'] if format['format_id'] == f)
            path = info['title']+'.'+ext
            ytdl.params['outtmpl'] = path

        ytdl.download([link])

        path = './'+path
        replacer = os.path.dirname(path)+'/'
        usr = message.chat.id
        await upload(uBot, usr, path, replacer)

        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)

    else:
        link = message.text.split()[1]

        def get_msg(title, formats):
            options = ''
            for format in formats:
                size = format['filesize']
                if size is None:
                    size = ''
                else:
                    size = str(round(size/(1024*1024), 2))+'MB'
                option = format['format_id']+' '+format['ext'] + \
                    ' '+format['format_note']+' '+size+'\n'
                options += option
            msg = title+"\n"+"Options: \n"+options
            return msg

        msg = link+'\n\n'
        info = ytdl.extract_info(link, download=False)
        if info.get('_type') == 'playlist':
            vids = info['entries']
            msg += info['title']+'\n\n'
            for vid in vids:
                msg += get_msg(vid['title'], vid['formats'])+'\n\n'
            if len(msg) > 4096:
                msgf = BytesIO(bytes(msg, 'utf-8'))
                msgf.name = info['title']+'.txt'
                await uBot.send_document(message.chat.id, msgf)
            else:
                await message.edit(msg)
        else:
            msg += get_msg(info['title'], info['formats'])
            await message.edit(msg)
