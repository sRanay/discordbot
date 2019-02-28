import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands

# Discord Bot Token
TOKEN = "NDYzNTk4NzQ1NDkwMjkyNzM2.Dhz-ZA.wl-tqxvxSuIRFu1IMjKPxLmSktk"

BOT_PREFIX = "?"
client = commands.Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


# Messages that the discord will reply to
"""@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # If message starts with "!hello"
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        # Print the message back to the text channel
        await client.send_message(message.channel, msg)

    # If message starts with "oof" or "OOF"
    if message.content.startswith('oof') or message.content.startswith('OOF'):
        msg = 'OOF'
        # Print the message back to the text channel
        await client.send_message(message.channel, msg)"""

# Starting up the discord bot
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with humans"))
    print('--------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)

# Running the bot
client.loop.create_task(list_servers())
client.run(TOKEN)