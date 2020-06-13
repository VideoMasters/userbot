import asyncio,os
from pyrogram import Client 
api_id=int(os.environ['API_ID'])
api_hash=os.environ['API_HASH']
HU_STRING_SESSION=os.environ['HU_STRING_SESSION']
uBot = Client(HU_STRING_SESSION,api_id,api_hash,plugins=dict(root="plugins"))
if __name__ == "__main__" :
    uBot.run()
