import discord

# The discord client
client = discord.Client()
# The token that allows client to run the script
# token = ...

# Notify on console that the discord bot is ready
@client.event
async def on_ready():
    print("The bot is ready!")

# Responds to commands
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!hello"):
        await message.channel.send('Hello!')


client.run(token)