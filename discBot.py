# Import libraries needed for our bot to work.
# discord: Helps the bot communicate with Discord.
# os: Allows the bot to work with our computer's environment, like files or settings.
# random: Used to pick random jokes.
# dotenv: Loads password (token) from a hidden file to keep them safe.
# ec2_metadata: Helps the bot get information about an AWS EC2 server.
# googletrans: Allows the bot to translate text between languages.

import discord
import os
import random
from dotenv import load_dotenv
from ec2_metadata import ec2_metadata
from googletrans import Translator

#Load the ".env" file where the bot's secret token (password) is stored securely.
load_dotenv()

#Tell the bot what kind of information it can access in Discord.
#Enabling the bot to read messages sent by people in channels.
intents = discord.Intents.default()
intents.message_content = True

#Create the bot and give it the permissions we set above.
client = discord.Client(intents=intents)

#Get the bot's secret token from the .env file to log into Discord.
token = str(os.getenv('TOKEN'))

#This event runs when the bot successfully connects to Discord.
@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))  #Print a message in the console to inform that the bot is online.

#This event runs every time someone sends a message in a channel.
@client.event 
#Extract useful information about the message.
async def on_message(message):
    username = str(message.author).split("#")[0] #Get the username (exclude everything before # in their name).
    channel = str(message.channel.name)  #Get the channel name where the message was sent.
    user_message = str(message.content) #Get the message content.
    
    #Print the message details in the console for debugging or tracking.
    print(f'Message {user_message} by {username} on {channel}')

    #Ignore messages sent by the bot to avoid loops and improve efficiency.
    if message.author == client.user: 
        return
    
    #Check if the message is in the "bot-testing" channel.
    if channel == "bot-testing":
        #Check if the message is a greeting like "hello", "hi", or "hello world".
        if user_message.lower() == "hello world" or user_message.lower() == "hi" or user_message.lower() == "hello":
            try:
                #Get the region of the EC2 server.
                region = ec2_metadata.region
                #Create a response to the greeting showing the region information.
                response = (f'Hello {username}, your EC2 Region: {ec2_metadata.region}')

            except Exception as e:
                #Print a message in the console if there is an error, and notify the user.
                print(f"Region not available: {e}")
                response = (f"Hello {username}. Sorry, I couldn't retrieve your region information.")
            #Send the response back to the user.
            await message.channel.send(response)

        #Check if the user wants to translate text.
        if user_message.lower().startswith('translate'):
            try:
                #Split the message into parts to find the target language and the text to translate.
                pieces = user_message.split(" ", 2)
                #If the message doesn't have enough info, explain how to use the command.
                if (len(pieces) < 2):
                    await message.channel.send('Please enter the language you want to translate to and text in the following format: "translate <language> <sentence to translate>"')
                    return
                #Get the language to translate to and the text to translate.                    
                language = pieces[1].lower()
                toTranslate = pieces[2]

                #Use Google Translator to translate the text.
                translation = Translator().translate(toTranslate, dest = language)
                #Reply with the translated text.
                await message.channel.send(f'Your text was translated to: {translation.text}')
            except Exception as e:
                 #If translation fails, print the error in the console and notify the user.
                print(f"Translation error: {e}")
                await message.channel.send("Sorry, I couldn't translate your text. Check the format: 'translate <language> <sentence to translate>'")
        #Check if the user wants information about the EC2 server.
        elif user_message.lower() == "tell me about my server!" or user_message.lower() == "tell me about my server":
            try:
                #Attemp to get the server's public IP, private IP, region, and availability zone.
                public_ip = ec2_metadata.public_ipv4 or "No public IP available"
                private_ip = ec2_metadata.private_ipv4 or "No private IP available"
                region = ec2_metadata.region or "Region data not available"
                availability_zone = ec2_metadata.availability_zone or "Availability zone not available"

                #Create a response with the server's details.
                response = (
                    f"Here are the details about your EC2 server:\n"
                    f"- **Public IP Address**: {public_ip}\n"
                    f"- **Private IP Address**: {private_ip}\n"
                    f"- **AWS Region**: {region}\n"
                    f"- **Availability Zone**: {availability_zone}"
            )
            except Exception as e:
                #If there’s an error, print the error in the console and notify the user.
                print(f"Error fetching EC2 metadata: {e}")
                response = "Sorry, I couldn't retrieve the EC2 server details. Please check the server configuration or try again later."

            #Send the response back to the user.
            await message.channel.send(response)

        #Check if the user asks for a joke.
        elif user_message.lower() == "tell me a joke" or user_message.lower() == "tell me a joke!":
            #Create an array with different jokes.
            jokes = ["Of all the inventions of the last hundred years, the dry erase board is the most remarkable.",
                     'My girlfriend kept complaining “you’re always acting like a detective. I want to split up” so I said “that’s a good idea, we’ll cover more ground that way',
                     "There was a king once who was 12 inches tall. Terrible king, great ruler."]
            #Send a random joke from the list
            await message.channel.send(random.choice(jokes))
    
#Run the bot using the token
client.run(token)

