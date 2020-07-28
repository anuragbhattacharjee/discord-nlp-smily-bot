import os

import discord
from dotenv import load_dotenv
from emojize import Emojize

e = Emojize()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    # for guild in client.guilds:
    #     if guild.name == GUILD:
    #         break

    # guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_message(message):
    print(message.author, client.user, type(client.user))
    if message.author == client.user:
        return

    emoji = e.predict(message.content)
    if emoji != '':
        await message.channel.send(emoji)
    if message.content.startswith('hello'):
        await message.channel.send('Hello World!')


client.run(TOKEN)
