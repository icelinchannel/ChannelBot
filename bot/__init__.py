new_env_file = open('bot/.env', 'w')

text = '''TG_TOKEN = "<your Telegram bot token here>"
WELCOME_IMAGE_LINK = "<a link to your image>"
ICELIN_GROUP_ID = "<your Telegram comments group id>"
ICELIN_CHANNEL_ID = "<your Telegram channel id here>"
PYTHON_VERSION = 3.11.3'''

new_env_file.write(text)
new_env_file.close()
