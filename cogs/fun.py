import os
import discord
from discord.ext import commands
import requests
import json
import random

tenorapi = os.environ['TENOR']


class Fun(commands.Cog):

  @commands.command(aliases=["HUG","hugs"])
  async def hug(self,ctx,*,user=""):
    gifs = gif("anime hug",tenorapi,50)
    if gifs == None:
      await ctx.send("Error finding gifs at this time, Try again")
    else:
      if user =="":
        await ctx.send("You need to mention someone")
      else:
        if str(user)[3:] == str(ctx.message.author.mention)[2:]:
          await ctx.send("Hey! ill give you a hug instead "+ ctx.author.mention)
          embed = set_embed(gifs['results'][random.randint(0,51)]['media'][0]['gif']['url'])
          await ctx.send(embed = embed)
        else:
          await ctx.send(ctx.message.author.mention + " hugs " + user)
          embed = set_embed("Awww! are'nt you a cutie. ❤️ ❤️",discord.Color.purple(),gifs['results'][random.randint(0,31)]['media'][0]['gif']['url'])
          await ctx.send(embed = embed)

  @commands.command(aliases=["slaps","SLAP"])
  async def slap(self,ctx,*,user=""):
    gifs = gif("anime slap",tenorapi,50)
    if gifs == None:
      await ctx.send("Error finding gifs at this time, Try again")
    else:
      if user =="":
        await ctx.send("You need to mention someone")
      else:
        if str(user)[3:] == str(ctx.message.author.mention)[2:]:
          await ctx.send("Why do you want to slap yourself?? "+ ctx.author.mention)
          embed = set_embed(gifs['results'][random.randint(0,51)]['media'][0]['gif']['url'])
          await ctx.send(embed = embed)
        else:
          await ctx.send(ctx.message.author.mention + " slaps " + user)
          embed = set_embed(ctx.message.author+ " is angry!!",discord.Color.red(),gifs['results'][random.randint(0,31)]['media'][0]['gif']['url'])
          await ctx.send(embed = embed)


def gif(search,api,limit=30):
  r = requests.get("https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api, limit))
  if r.status_code == 200:
    # load the GIFs using the urls for the smaller GIF sizes
    gifs = json.loads(r.content)
    print()
  else:
    gifs = None
  return gifs

def set_embed(title,color,gif):
  embed=discord.Embed(title=title,color=color)
  embed.set_image(url=gif)
  embed.set_footer(text ="Gifs supplied by Tenor")
  return embed


def setup(client):
  client.add_cog(Fun(client))