import discord
from discord.ext import commands
import random

#class for any utility related feature.
class Utility(commands.Cog):

  #initializing discord client into class instance
  def __init__(self,client):
    self.client=client

  #command for flipping a coin
  @commands.command(aliases = ["toss","coinflip"])
  async def flip(self,ctx):
    await ctx.send("Heads" if random.randint(1,2)%2==0 else "Tails")

  @commands.command()
  async def ping(self,ctx):
    if str(ctx.author)=="manas#3570":
      await ctx.author.send("Hey manu, Hope u have a great day. Have my greatest birthday wishes to a special someone. <3 <3")
    else:
      print(ctx.author)
      await ctx.author.send("Pong!")

#setting up all the cogs(functions) 
def setup(client):
  client.add_cog(Utility(client)) 