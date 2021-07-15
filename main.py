import discord
import requests
import json
import os
import cryptocompare
from crypto import *



KEY = os.getenv('CRYPTOCOMPARE_API_KEY')
TOKEN = os.getenv('TOKEN')

cryptocompare.cryptocompare._set_api_key_parameter(KEY)

client = discord.Client()

command = '!Crypto:'

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Activity(activity = discord.ActivityType.listening, name = 'Searching Current Crypto Prices...'))

@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith(command):
        coin = message.content.replace(command, '').lower()
        if len(coin) >= 1:
            url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms=USD&api_key={}'.format(coin, KEY)
            try:
                data = json.loads(requests.get(url).content)['USD']

                await message.channel.send(embed=crypto_message(data, coin))
            except KeyError:
                await message.channel.send(embed=error_message(coin))

client.run(TOKEN)
