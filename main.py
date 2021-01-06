import requests
import random
import WebScraper
import discord
client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        await message.channel.send('...')

    if message.content.startswith('!game'):
        await message.channel.send (WebScraper.top100games())
        
client.run('')