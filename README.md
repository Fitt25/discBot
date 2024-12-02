#Discord Bot Project

#Overview
This project is a Discord bot developed using Python and the `discord+` library, designed to provide useful features like server information and a text translation tool for Discord servers. The bot also fetches server metadata from an EC2 instance, providing additional details about the environment. It was created as part of my IT 115 course project to showcase my skills in Python programming, working with APIs, and deploying on an EC2 instance.

#Purpose
The purpose of this bot is to enhance the user experience in Discord servers by providing easy access to server metadata from an EC2 instance, and a translation feature for converting text into different languages. This project is a practice in Python, APIs, and integrating with cloud environments like AWS EC2.

#Features
- Greetings: The bot can reply to a variety of greetings and include the user info. 
- Server Information: The bot can provide details about the Discord server, such as the server name, member count, and server owner.
- Server Metadata: The bot fetches server metadata (e.g., instance ID, region, type) from an EC2 instance. This requires the bot to be connected to an EC2 environment to display the relevant data.
- Text Translation: Users can input text, and the bot will translate it into a target language using an external translation API.

#How It Works

The bot is built with Python and uses the `discord` library to interact with Discord's API. Here’s how it functions:
1. Set up and Authentication: The bot connects to Discord using a bot token after being added to a server.
2. Server Information Command: Users can use the `Tell me about my server` command to receive information about the server.
3. Server Metadata Command: The bot fetches metadata from an EC2 instance (e.g., instance ID, region) by accessing the EC2 API. The bot needs to be deployed on an EC2 instance for this feature to work.
4. Translation Command: The bot listens for the `translate` command, followed by the the target language and the text to be translated. It uses a translation API to provide the translated text.

#Setup
To run this bot on your server, follow these steps:

#Prerequisites
- [Python](https://www.python.org/downloads/) installed on your system
- A Discord account and a bot created in the [Discord Developer Portal](https://discord.com/developers/applications)
- A bot token from the Discord Developer Portal
- An API for the translation service: Google Translate API
- An AWS EC2 instance set up to fetch server metadata (instance ID, region, etc.) and EC2 MetaData library.
- A Pip Package Manager and PyCord
