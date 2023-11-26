from aiogram import Bot, Dispatcher, Router

from dotenv import load_dotenv
from os import getenv


load_dotenv()

API_TOKEN = getenv('TG_TOKEN')
WELCOME_IMAGE_LINK = getenv('WELCOME_IMAGE_LINK')  # image is in cloud storage, if you use this code, add your link here
GROUP_ID = int(getenv("ICELIN_GROUP_ID"))
CHANNEL_ID = int(getenv('ICELIN_CHANNEL_ID'))


bot = Bot(API_TOKEN)
dp = Dispatcher()


private_rt = Router()
group_rt = Router()
channel_rt = Router()
