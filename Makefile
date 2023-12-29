install:
	pip install poetry
	clear
	poetry install

update:
	poetry update package
	sudo apt update
	sudo apt upgrade

start:
	poetry update package
	clear
	poetry run python bot/main.py
