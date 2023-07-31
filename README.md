# SandScripter

## Description
SandScripter is a Discord bot built using Discord.py that provides various functionalities to enhance your Discord server.

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Dependencies
- discord.py (2.1.0 or later)
- dotenv

### Setup
1. Clone this repository to your local machine.
2. Install the required dependencies
3. Create a new Discord bot on the [Discord Developer Portal](https://discord.com/developers/applications).
4. Obtain your bot token from the Developer Portal.
5. Create a `.env` file in the root directory and add the following line: ```DISCORD_TOKEN=your_bot_token_here```

## Usage
- To start the bot, run the following command in the terminal: ```python bot.py```

- The bot will now be online and ready to respond to commands in the Discord server.

## Features
- **create_guild_channel** : Create a new channel in the server
- **delete_guild_channel** : Delete a channel in the server
- **create_guild_category** : Create a new category in the server
- **delete_guild_category** : Delete a category in the server
- **purge_channel** : Delete a specific amount of messages
- **kick_user** : Kick an user of the server
- **ban_user** : Ban an user of the server
- **poll** : Make a poll on the server

## Commands
- The bot uses Slash Commands, which are integrated in Discord. To use a specific command, start your message with "/" followed by the feature you want to use.