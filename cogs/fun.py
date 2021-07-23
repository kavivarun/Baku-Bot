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
          embed = set_embed("Awww! are'nt you a cutie. ❤️ ❤️",discord.Color.purple(),gifs['results'][random.randint(0,51)]['media'][0]['gif']['url'])
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
          embed = set_embed(str(ctx.message.author) + " is angry!!",discord.Color.red(),gifs['results'][random.randint(0,51)]['media'][0]['gif']['url'])
          await ctx.send(embed = embed)
        else:
          await ctx.send(ctx.message.author.mention + " slaps " + user)
          embed = set_embed(str(ctx.message.author) + " is angry!!",discord.Color.red(),gifs['results'][random.randint(0,31)]['media'][0]['gif']['url'])
          await ctx.send(embed = embed)

  @commands.command(aliases=["punches","PUNCH"])
  async def punch(self,ctx,*,user=""):
    gifs = gif("anime punch",tenorapi,50)
    if gifs == None:
      await ctx.send("Error finding gifs at this time, Try again")
    else:
      if user =="":
        await ctx.send("You need to mention someone")
      else:
        if str(user)[3:] == str(ctx.message.author.mention)[2:]:
          await ctx.send("Why do you want to punch yourself?? "+ ctx.author.mention)
          embed = set_embed(str(ctx.message.author) + " is furious!!",discord.Color.blurple(),gifs['results'][random.randint(0,51)]['media'][0]['gif']['url'])
          await ctx.send(embed = embed)
        else:
          await ctx.send(ctx.message.author.mention + " punches " + user)
          embed = set_embed(str(ctx.message.author) + " is furious!!",discord.Color.blurple(),gifs['results'][random.randint(0,31)]['media'][0]['gif']['url'])
          await ctx.send(embed = embed)

  @commands.command(aliases=["kicks","KICK"])
  async def kick(self,ctx,*,user=""):
    gifs = gif("anime kick",tenorapi,50)
    if gifs == None:
      await ctx.send("Error finding gifs at this time, Try again")
    else:
      if user =="":
        await ctx.send("You need to mention someone")
      else:
        if str(user)[3:] == str(ctx.message.author.mention)[2:]:
          await ctx.send("Why do you want to kick yourself?? "+ ctx.author.mention)
          embed = set_embed(str(ctx.message.author) + " is on a rampage!!",discord.Color.orange(),gifs['results'][random.randint(0,51)]['media'][0]['gif']['url'])
          await ctx.send(embed = embed)
        else:
          await ctx.send(ctx.message.author.mention + " kicks " + user)
          embed = set_embed(str(ctx.message.author) + " is on a rampage!!",discord.Color.orange(),gifs['results'][random.randint(0,31)]['media'][0]['gif']['url'])
          await ctx.send(embed = embed)
  @commands.command(aliases=["kisses","KISS"])
  async def kiss(self,ctx,*,user=""):
    gifs = gif("anime kiss",tenorapi,50)
    if gifs == None:
      await ctx.send("Error finding gifs at this time, Try again")
    else:
      if user =="":
        await ctx.send("You need to mention someone")
      else:
        if str(user)[3:] == str(ctx.message.author.mention)[2:]:
          await ctx.send("Hey! ill give you a kiss instead "+ ctx.author.mention)
          embed = set_embed("Things are getting spicy in here. 💋💋",discord.Color.red() , gifs['results'][random.randint(0,51)]['media'][0]['gif']['url'])
          await ctx.send(embed = embed)
        else:
          await ctx.send(ctx.message.author.mention + " kisses " + user)
          embed = set_embed("Things are getting spicy in here. 💋💋",discord.Color.red() , gifs['results'][random.randint(0,31)]['media'][0]['gif']['url'])
          await ctx.send(embed = embed)
  
  @commands.command(aliases=["bites","BITE"])
  async def bite(self,ctx,*,user=""):
    gifs = gif("anime bite",tenorapi,50)
    if gifs == None:
      await ctx.send("Error finding gifs at this time, Try again")
    else:
      if user =="":
        await ctx.send("You need to mention someone")
      else:
        if str(user)[3:] == str(ctx.message.author.mention)[2:]:
          await ctx.send("Why do you bite yourself? "+ ctx.author.mention)
          embed = set_embed("Dosent that hurt?",discord.Color.blue(),gifs['results'][random.randint(0,51)]['media'][0]['gif']['url'])
          await ctx.send(embed = embed)
        else:
          await ctx.send(ctx.message.author.mention + " bites " + user)
          embed = set_embed(str(ctx.message.author) + " is itching to taste flesh ",discord.Color.blue(),gifs['results'][random.randint(0,31)]['media'][0]['gif']['url'])
          await ctx.send(embed = embed)
 
  @commands.command(aliases=["licks","LICK"])
  async def lick(self,ctx,*,user=""):
    gifs = gif("anime lick",tenorapi,50)
    if gifs == None:
      await ctx.send("Error finding gifs at this time, Try again")
    else:
      if user =="":
        await ctx.send("You need to mention someone")
      else:
        if str(user)[3:] == str(ctx.message.author.mention)[2:]:
          await ctx.send("Did you taste salty? "+ ctx.author.mention)
          embed = set_embed("You remind me of my cat",discord.Color.green(),gifs['results'][random.randint(0,51)]['media'][0]['gif']['url'])
          await ctx.send(embed = embed)
        else:
          await ctx.send(ctx.message.author.mention + " licks " + user)
          embed = set_embed("Weird fetish but okay",discord.Color.green(),gifs['results'][random.randint(0,31)]['media'][0]['gif']['url'])
          await ctx.send(embed = embed)
  
  @commands.command(aliases=["headpats","HEADPAT"])
  async def headpat(self,ctx,*,user=""):
    gifs = gif("anime headpat",tenorapi,50)
    if gifs == None:
      await ctx.send("Error finding gifs at this time, Try again")
    else:
      if user =="":
        await ctx.send("You need to mention someone")
      else:
        if str(user)[3:] == str(ctx.message.author.mention)[2:]:
          await ctx.send("Ill pat you instead"+ ctx.author.mention)
          embed = set_embed("There There li'l cutie",discord.Color.blurple(),gifs['results'][random.randint(0,51)]['media'][0]['gif']['url'])
          await ctx.send(embed = embed)
        else:
          await ctx.send(ctx.message.author.mention + " headpats " + user)
          embed = set_embed("There There li'l cutie",discord.Color.blurple(),gifs['results'][random.randint(0,31)]['media'][0]['gif']['url'])
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