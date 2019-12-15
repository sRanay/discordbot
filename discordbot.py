import discord
import time
import asyncio

# Discord Bot Token
TOKEN = "NDYzNTk4NzQ1NDkwMjkyNzM2.Dhz-ZA.wl-tqxvxSuIRFu1IMjKPxLmSktk"

# Creating the client Object
client = discord.Client()

joined = messages = 0

async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("stats.txt","a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")

                messages = 0
                joined = 0

                await asyncio.sleep(5)
        except Exception as e:
            print(e)
            await asyncio.sleep(5)

@client.event
async def on_member_update(before, after):
    n = after.nick
    if n: # Check if they updated their username
        if n.lower().count("tim") > 0: # If username contiains tim
            last = before.nick
            if last:
                await after.edit(nick=last)
            else:
                await after.edit(nick="NO STOP THAT")

@client.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send_message(f"""Welcome to the server {member.mention}""")

@client.event
async def on_message(message):
    global messages
    messages += 1
    id = client.get_guild(456983227899314178)
    channels = ['bot-commands', 'discord-bot-test']
    valid_users = ['Ranay#8872']
    bad_words = ['bad','stop','45']

    # Removing words in the bad list
    for word in bad_words:
        if message.content.count(word) > 0:
            print("A bad word was said")
            await message.channel.purge(limit=1)

    if message.content == "!help":
        embed = discord.Embed(title="Help on BOT", description="Some useful commands")
        embed.add_field(name="!hello", value="Greets the user")
        embed.add_field(name="!users", value="Prints number of users", inline=False)
        await message.channel.send(content=None, embed=embed)

    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("!hello") != -1:
            await message.channel.send("Hi") #If user says !hello, will send back hi
        elif message.content == "!users":
            await message.channel.send(f"""# of Members: {id.member_count}""")


# Running the Bot
client.loop.create_task(update_stats())
client.run(TOKEN)