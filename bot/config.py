from dotenv import load_dotenv
from os import getenv

load_dotenv()
API_TOKEN = getenv('TG_TOKEN')
WELCOME_IMAGE_LINK = getenv('WELCOME_IMAGE_LINK') # image is in cloud storage, if you use this code, add your link here
CHAT_ID = int(getenv("ICELIN_CHAT_ID"))
CHANNEL_ID = int(getenv('ICELIN_CHANNEL_ID'))
