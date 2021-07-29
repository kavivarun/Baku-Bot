import os
import discord
from discord.ext import commands
import requests
import json
import random


tenorapi = os.environ['TENOR']
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
    await ctx.author.send("Pong!")

  @commands.command(aliases=["g","GIF","gifs"])
  async def gif(self,ctx,*,search):
    g=gifs(search,tenorapi,50)
    if g == None:
      await ctx.send("Error finding gifs at this time, Try again")
    else:
      embed=discord.Embed(title="here you go",color=discord.Color.red())
      embed.set_image(url=g['results'][random.randint(0,51)]['media'][0]['gif']['url'])
      embed.set_footer(text ="Gifs supplied by Tenor")
      await ctx.send(embed=embed)


def gifs(search,api,limit=50):
  r = requests.get("https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api, limit))
  if r.status_code == 200:
    # load the GIFs using the urls for the smaller GIF sizes
    gifs = json.loads(r.content)
    print()
  else:
    gifs = None
  return gifs

#setting up all the cogs(functions) 
def setup(client):
  client.add_cog(Utility(client)) 