import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

#chaning intents for dm interaction
intents = discord.Intents.all()
intents.members = True
#Loading client and setting Prefix for bot
client = discord.Client()
client = commands.Bot(command_prefix=["baku ","Baku ","BAKU "],intents=intents)

#Loading the differnt extensions in cogs directory
for filename in os.listdir("./cogs"):
  if filename.endswith('.py'):
    client.load_extension('cogs.{0}'.format(filename[:-3]))

#listener for when bot is ready
@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online,activity= discord.Game("The Sauce Finder"))
  print('logged in as {0.user}'.format(client))

#Keeping server running using flask
keep_alive()

#Telling client what Bot to run using the bots token
client.run(os.getenv('TOKEN'))  
