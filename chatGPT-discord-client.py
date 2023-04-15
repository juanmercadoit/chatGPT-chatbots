# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from cfg import APIGPT, APIDISCORD
import openai
import discord

class ClienteDiscord(discord.Client):
    async def on_read(self):
        print("Cliente conectado")
    async def on_message(self,message):
        print(message.author)
        print(message.content)

intents = discord.Intents.default()
intents.message_content = True

cliente = ClienteDiscord(intents = intents)

cliente.run(APIDISCORD)