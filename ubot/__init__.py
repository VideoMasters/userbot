import os
from ubot.config import Config
API_ID=int(os.environ.get('API_ID',Config.API_ID))
API_HASH=os.environ.get('API_HASH',Config.API_HASH)
HU_STRING_SESSION=os.environ.get('HU_STRING_SESSION',Config.HU_STRING_SESSION)
