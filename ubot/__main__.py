from pyrogram import Client

from ubot import API_HASH, API_ID, HU_STRING_SESSION

uBot = Client(HU_STRING_SESSION, API_ID, API_HASH,
              plugins=dict(root="ubot/plugins"))
if __name__ == "__main__":
    uBot.run()
