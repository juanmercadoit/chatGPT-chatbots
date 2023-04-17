# -*- coding: utf-8 -*-
"""
Spyder Editor

Juan Andres Mercado, Connection file in python.
"""

from paramsCFG import APIGPT, APIDISCORD
from dotenv import load_dotenv
import openai
import discord
import os

# 1) This code help you to confirm you connection with your Discord server and credentials. 
class ClienteDiscord(discord.Client):
    async def on_read(self):
        print("Cliente conectado")
    async def on_message(self,message):
        print(message.author)
        print(message.content)

intents = discord.Intents.default()
intents.message_content = True

cliente = ClienteDiscord(intents = intents)

# 2)  Interaction level with the bot, mentions, answer, questions, send and receive messages.

# Set up the OpenAI API client and credentials.
openai.api_key = APIGPT

# this is the code we will use first to test the connection.
@cliente.event
async def on_message(message):
  # The bot don´t response itself. The bot response to other users only.
  if message.author == cliente.user:
    return
# Example to sending and receive a structured message from the bot:
# Delete the comments below for testing.
#  if message.content.startswith('Hello DonaML'):
#    await message.channel.send('Howdy Human Friend')

# Validate if the bot is mentioned in the message Egg. @DDonaML
  if cliente.user in message.mentions:

# If the bot is mentioned in the message, use the OpenAI API to generate a response to the message.
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{message.content}",
        max_tokens=2048,
        temperature=0.5,
        )
    # Send the response received as a message
    await message.channel.send(response.choices[0].text)

# Start the bot in Discord Server.
cliente.run(APIDISCORD)