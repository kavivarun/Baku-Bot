import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

#Loading client and setting Prefix for bot
client = discord.Client()
client = commands.Bot(command_prefix="baku ")

#Loading the differnt extensions in cogs directory
for filename in os.listdir("./cogs"):
  if filename.endswith('.py'):
    client.load_extension('cogs.{0}'.format(filename[:-3]))

#Keeping server running using flask
keep_alive()

#Telling client what Bot to run using the bots token
client.run(os.getenv('TOKEN'))  
