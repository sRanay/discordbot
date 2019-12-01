import random
import asyncio
import discord
import opuslib
import youtube_dl
from discord.ext import commands
from itertools import cycle

# Discord Bot Token
TOKEN = "NDYzNTk4NzQ1NDkwMjkyNzM2.Dhz-ZA.wl-tqxvxSuIRFu1IMjKPxLmSktk"

#Creating the client Object
BOT_PREFIX = "."
client = commands.Bot(command_prefix=BOT_PREFIX)
client.remove_command('help')

#Creating the list of status messages
status = ['with my life', 'with my dong',]

# Store instance of players
players = {}

# Store the Queues
queues = {}

"""
# Check the music bot queue
def check_queue(serverid):
    if queues[serverid] != []:
        player = queues[serverid].pop(0)
        players[serverid] = player
        player.start()
"""

# Change status once in a while
async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)

    # If the bot is up
    while not client.is_closed:
        current_status = next(msgs) # Gets the next message
        await client.change_presence(game=discord.Game(name=current_status)) # Set it to the current status
        await asyncio.sleep(5) # Change the status message based every 5 seconds

"""
# Speak something once in a while
async def NormalMessage():
    await client.wait_until_ready()
    channel = client.get_channel("456983229032038421")

    while not client.is_closed:
        await client.send_message(channel, "FK LAHHHHHHHHHHHHHHH")
        await asyncio.sleep(300)
"""

# Start of Commands
# clear command
@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    # It will delete every message that is not long than 14 days
    # It will only delete 100 messages from the channel
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say("Messages Deleted")

# Embed Function/Command
@client.command(pass_context=True)
async def eventcreate(ctx, arg1, arg2):
    author = ctx.message.author
    embed = discord.Embed(
        title = arg1, # The title of the embed
        description = arg2, # Description of the embed
        colour = discord.Colour.blue() # The color of the embed at the side
    )
    
    # inline will determine whether the Field are in the same line
    embed.add_field(name='Confirmed', value='None', inline=True)
    embed.add_field(name='Reserve', value='None', inline=True)
    embed.add_field(name='Created by', value=author, inline=False)

    await client.say(embed=embed)

# Help Function
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='Help')
    # List of Commands using Help
    embed.add_field(name='clear', value='Clear the latest 100 messages less than 14 days ago', inline=False)
    embed.add_field(name='displayembed', value='Display the template for embed', inline=False)
    embed.add_field(name='join', value='Joins current channel', inline=False)
    embed.add_field(name='leave', value='Leaves current channel', inline=False)

    await client.send_message(author, embed=embed)
"""
# Join Command
@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

# Leave Command
@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

# Music Bot does not work now

# Music Bot Functions
# play - Play the music given the URL
# pause - Pause the current music
# stop - Stop the current music
# resume - Resume the current music

# play Command
@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
    players[server.id] = player
    player.start()

# pause Command
@client.command(pass_context=True)
async def pause(ctx):
    serverid = ctx.message.server.id
    players[serverid].pause()

# stop Command
@client.command(pass_context=True)
async def stop(ctx):
    serverid = ctx.message.server.id
    players[serverid].stop()

# resume Command
@client.command(pass_context=True)
async def resume(ctx):
    serverid = ctx.message.server.id
    players[serverid].resume()

# queue Command
@client.command(pass_context=True)
async def queue(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))

    if server.id in queues:
        queues[server.id].append(player)
    else:
        queues[server.id] = [player]
    await client.say('Video Queued.')
"""
# End of Commands

# Start of Events 

# On member join
@client.event
async def on_member_join(member):
    # Set the role to be normal
    role = discord.utils.get(member.server.roles, name='Normal')
    # Implement it for the current member that is joining
    await client.add_roles(member,role)

# Reaction
@client.event
async def on_reaction_add(reaction,user):
    channel = reaction.message.channel
    await client.send_message(channel, '{} has added {} to the messasge: {}'.format(user.name, reaction.emoji, reaction.message.content))

@client.event
async def on_reaction_remove(reaction,user):
    channel = reaction.message.channel
    await client.send_message(channel, '{} has removed {} from the messasge: {}'.format(user.name, reaction.emoji, reaction.message.content))

# End of Events

# Starting up the discord bot
@client.event
async def on_ready():
    print('Bot is ready')

# Running the bot
client.loop.create_task(change_status())
#client.loop.create_task(NormalMessage())
client.run(TOKEN)