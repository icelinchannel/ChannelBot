install:
	pip install poetry
	poetry install

update:
	poetry update package
	sudo apt update
	sudo apt upgrade
