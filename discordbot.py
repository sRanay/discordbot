import random
import asyncio
import discord
from discord.ext import commands
from itertools import cycle

# Discord Bot Token
TOKEN = "NDYzNTk4NzQ1NDkwMjkyNzM2.Dhz-ZA.wl-tqxvxSuIRFu1IMjKPxLmSktk"

BOT_PREFIX = "."
client = commands.Bot(command_prefix=BOT_PREFIX)
status = ['Msg1', 'Msg2', 'Msg3']

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)

    # If the bot is up
    while not client.is_closed:
        current_status = next(msgs) # Gets the next message
        await client.change_presence(game=discord.Game(name=current_status)) # Set it to the current status
        await asyncio.sleep(5) # Change the status message based every 5 seconds

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

@client.command()
async def displayembed():
    embed = discord.Embed(
        title = 'Title', # The title of the embed
        description = 'This is a description.', # Description of the embed
        colour = discord.Colour.blue() # The color of the embed at the side
    )

    # Embed Settings
    embed.set_footer(text='This is a footer.') #Appears below the image
    embed.set_image(url='http://www.personalbrandingblog.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640-300x300.png') #Appears above the Footer
    embed.set_thumbnail(url='http://www.personalbrandingblog.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640-300x300.png') #Thumbnail of the embed
    embed.set_author(name='Author Name',
        icon_url='http://www.personalbrandingblog.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640-300x300.png') #Set the Author Name and Icon
    # inline will determine whether the Field are in the same line
    embed.add_field(name='Field Name', value='Field Value', inline=False)
    embed.add_field(name='Field Name', value='Field Value', inline=True)
    embed.add_field(name='Field Name', value='Field Value', inline=True)

    await client.say(embed=embed)

#On member join
@client.event
async def on_member_join(member):
    # Set the role to be normal
    role = discord.utils.get(member.server.roles, name='Normal')
    # Implement it for the current member that is joining
    await client.add_roles(member,role)

# Starting up the discord bot
@client.event
async def on_ready():
    print('Bot is ready')


# Running the bot
client.loop.create_task(change_status())
client.run(TOKEN)