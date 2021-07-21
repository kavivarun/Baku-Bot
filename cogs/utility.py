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


#setting up all the cogs(functions) 
def setup(client):
  client.add_cog(Utility(client))