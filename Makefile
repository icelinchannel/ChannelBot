install:
	pip install poetry
	poetry install

update:
	poetry update package
	sudo apt update
	sudo apt upgrade

start:
	poetry update package
	cd bot
	clear
	poetry run python main.py
