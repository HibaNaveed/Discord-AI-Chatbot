# This example requires the 'message_content' intent.

import discord
from dotenv import load_dotenv
import os
from google import genai
load_dotenv()
discord_key=os.getenv("discord_secret_key")
google_key=os.getenv("google_api_key")

intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
        if client.user != message.author:
            if client.user in message.mentions:
                                

                client_google = genai.Client(api_key=google_key)

                interaction = client_google.interactions.create(
                    model="gemini-3.6-flash",
                    input=message.content
                )
                print(interaction.output_text)
                await message.channel.send(interaction.output_text)

client.run(discord_key)
