import discord
import time
import asyncio
import random

from discord.ext import commands

# Discord Bot Token
TOKEN = "NDYzNTk4NzQ1NDkwMjkyNzM2.Dhz-ZA.wl-tqxvxSuIRFu1IMjKPxLmSktk"

# Creating the client Object
client = commands.Bot(command_prefix=".")
client.remove_command("help")

# Discord Command

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Help on BOT", description="Some useful commands")
    embed.add_field(name=".hello", value="Greets the user")
    embed.add_field(name=".users", value="Prints number of users", inline=False)
    embed.add_field(name=".userinfo", value="Print the user info of member", inline=False)
    embed.add_field(name=".echo", value="Repeats the statement", inline=False)
    embed.add_field(name=".help", value="Print out this page", inline=False)
    await ctx.channel.send(content=None, embed=embed)

@client.command(pass_context=True)
async def hello(ctx):
    await ctx.channel.send("Hi") #If user says !hello, will send back hi

@client.command(pass_context=True)
async def users(ctx):
    id = client.get_guild(456983227899314178)
    await ctx.channel.send(f"""# of Members: {id.member_count}""")

@client.command(aliases=['echo'])
async def say(ctx, *, words: commands.clean_content):
    await ctx.send(words)

# Prints out user information
@client.command()
async def userinfo(ctx, member: discord.Member):
    roles = [role for role in member.roles]

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f'User Info - {member}')
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
    
    embed.add_field(name="ID: ", value=member.id)
    embed.add_field(name="Guild name: ", value=member.display_name)
    
    embed.add_field(name="Created at: ", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined at: ", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Top role: ", value=member.top_role.mention)

    embed.add_field(name="Bot?", value=member.bot)

    await ctx.send(embed=embed)

# End of Discord Command

# Discord event
@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send_message(f"""Welcome to the server {member.mention}""")

@client.event
async def on_message(message):
    id = client.get_guild(456983227899314178)
    channels = ['bot-commands', 'discord-bot-test','bot-command']
    valid_users = ['Ranay#8872']
    bad_words = ['bad','stop','45']

    # Removing words in the bad list
    for word in bad_words:
        if message.content.count(word) > 0:
            print("A bad word was said")
            await message.channel.purge(limit=1)

    await client.process_commands(message)

# End of Discord Event

# Running the Bot
client.run(TOKEN)