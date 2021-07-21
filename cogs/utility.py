import discord
from discord.ext import commands
import random

class Utility(commands.Cog):

  def __init__(self,client):
    self.client=client

  @commands.command(aliases = ["toss","coinflip"])
  async def flip(self,ctx):
    await ctx.send("Heads" if random.randint(1,2)%2==0 else "Tails")


def setup(client):
  client.add_cog(Utility(client))