import discord
from discord import app_commands
from modules.badwords import handle_badwords
from modules.commands import handle_commands
from modules.response import handle_response

with open("token.key", "r", encoding="utf-8") as f:
    TOKEN = f.read()
client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)
guild = client.get_guild(1113170764162662410)

@client.event
async def on_ready():
    await tree.sync(guild=guild)
    print(f"{client.user} is now running!")

@client.event
async def on_member_join(member):
    direct_message = await member.create_dm()
    await direct_message.send(f"# Welcome to The Workshop!\nHello <@{member.id}>\nThe Workshop, is a coding community dedicated to exploring the exciting world of AI and other coding elements! We're thrilled to have you here and can't wait to embark on this coding journey together.\n\nRemember to read the rules! https://discord.com/channels/1113170764162662410/1113178829771526214")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    await handle_badwords(message)
    
    if client.user.mentioned_in(message):
        await handle_response(message, client)

handle_commands(tree, app_commands, discord, guild)
client.run(TOKEN)