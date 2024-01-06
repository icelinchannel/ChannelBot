<p align="center">
    <a href="https://github.com/icelinchannel/ChannelBot/releases">
        <img alt="release" src="https://img.shields.io/github/v/release/icelinchannel/ChannelBot?color=pink&label=Latest Release&style=for-the-badge&sort=semver">
    </a>
    <a href="LICENSE">
        <img alt="license" src="https://img.shields.io/github/license/icelinchannel/ChannelBot?color=pink&style=for-the-badge">
    </a>
</p>

<h1 align="center">Channel Bot</h1>


## ✍ About

This is an aiogram-based bot for managing your telegram channel and it's group for comments. Using this bot you can anonymously communicate with your followers and rule them in comments group.


## 🛠 Build commands

Download project:
```shell
git clone https://github.com/icelinchannel/ChannelBot
```
<br>

Install dependencies:
```shell
make install
```
<br>

Update packages:
```shell
make update
```
<br>

Start project:
```shell
make start
```
<br>

Lint the project
```shell
make lint
```

Add constants to .env file
```shell
make add-constants
```


## 🖥 How to build this project

1. If you want to use this bot for your channel just follow the instruction below:

2. First, you need to create your bot's account via [BotFather](https://t.me/BotFather). Also, you can customize it there

3. Next, you need to choose a service for deploying. You can use something like [Railway](https://railway.app/), [Heroku](https://www.heroku.com/) or [Render](https://render.com/). You should start a new web service there

4. Add built command - `make install`, and start command - `make start`

5. Add some variables to enviroment:
- `TG_TOKEN` = "*\<your Telegram bot token here>*"
- `WELCOME_IMAGE_LINK` = "*\<a link to your image>*"
- `ICELIN_GROUP_ID` = "*\<your Telegram comments group id>*"
- `ICELIN_CHANNEL_ID` = "*\<your Telegram channel id here>*"
- `OWNER_TG_ID` = "*<Telegram ID of a person, who is going to anonimously contact with bot's users>*"
- `PYTHON_VERSION` = 3.11.3
