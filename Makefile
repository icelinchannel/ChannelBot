install:
	pip install poetry
	clear
	poetry install

update:
	poetry update package

start:
	poetry update package
	clear
	poetry run python bot/main.py

lint:
	clear
	poetry run flake8 bot

add-constants:
	>> .env
	echo "TG_TOKEN = '<your Telegram bot token here>'" >> .env
	echo "WELCOME_IMAGE_LINK = '<a link to your image>'" >> .env
	echo "ICELIN_GROUP_ID = '<your Telegram comments group id>'" >> .env
	echo "ICELIN_CHANNEL_ID = '<your Telegram channel id here>'" >> .env
	echo "OWNER_TG_ID = '<Telegram ID of a person, who has to anonimously contact with bot's users>'" >> .env
	echo "PYTHON_VERSION = 3.11.3" >> .env
