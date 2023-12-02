new_env_file = open('../.env', 'w')

with open('../.python-version', 'r') as python_version_file:
    python_version = python_version_file.read()

text = f'''TG_TOKEN = "<your Telegram bot token here>"
WELCOME_IMAGE_LINK = "<a link to your image>"
ICELIN_GROUP_ID = "<your Telegram comments group id>"
ICELIN_CHANNEL_ID = "<your Telegram channel id here>"
PYTHON_VERSION = {python_version}'''

new_env_file.write(text)
new_env_file.close()
