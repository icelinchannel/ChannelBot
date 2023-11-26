new_env_file = open('.env', 'w')

text = '''TG_TOKEN = "<your Telegram bot token here>"
WELCOME_IMAGE_LINK = "<a link to your image>"
ICELIN_CHAT_ID = "<your Telegram comments group id>"
ICELIN_CHANNEL_ID = "<your Telegram channel id here>"
'''

new_env_file.write(text)
new_env_file.close()
