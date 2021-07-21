import discord
from discord.ext import commands
import os
import random
from NHentai.nhentai import NHentai
import asyncio

nhentai = NHentai()

#class for all commands related to hentai
class Hentai(commands.Cog):

  #initializing discord client into class instance
  def __init__(self,client):
    self.client = client
  
  @commands.Cog.listener()
  async def on_ready(self):
    await self.client.change_presence(status=discord.Status.online,activity= discord.Game("The Sauce Finder"))
    print('logged in as {0.user}'.format(self.client))

  @commands.command()
  async def sauce(self,ctx,*,hid=""):
    Doujin = 0
    i=0
    if hid == "":
      Doujin = nhentai.get_random()
    elif hid =="popular":
      popular = nhentai.get_popular_now()
      Doujin =nhentai.get_doujin(id=popular.doujins[random.randint(0,popular.total_doujins-1)].id )
    elif len(str(hid))==6 and str(hid).isdigit():
      Doujin= nhentai.get_doujin(id=hid)
    else:
      try:
        hsearch = nhentai.search(query=hid , sort='popular', page=1)
        size = hsearch.total_results
        total = hsearch.total_pages
        Doujin = nhentai.get_doujin(id = hsearch.doujins[random.randint(0,(size-1)//total)].id)
      except:
        await ctx.send("Enter a valid id or search string else leave search field empty ")

    if Doujin:
      embed=discord.Embed(title=Doujin.title,url='https://nhentai.net/g/{0}/'.format(Doujin.id),description=str(Doujin.total_pages)+ " Pages",color=discord.Color.red())
      embed.add_field(name="**Id**\n",value=Doujin.id+"\n",inline=True)
      embed.add_field(name="**Tags**",value="`"+"` `".join (Doujin.tags)+'`',inline=False)
      embed.set_footer(text='Artists: {0}'.format(", ".join(Doujin.artists) if len(Doujin.artists)>0 else "Unknown"))
      embed.set_thumbnail(url=Doujin.images[0])
      await ctx.send(embed=embed)

  @commands.command()
  async def read(self,ctx,*,hid=""):
    Doujin = 0
    i=0
    if hid == "":
      Doujin = nhentai.get_random()
    elif hid =="popular":
      popular = nhentai.get_popular_now()
      Doujin =nhentai.get_doujin(id=popular.doujins[random.randint(0,popular.total_doujins-1)].id )
    elif len(str(hid))==6 and str(hid).isdigit():
      Doujin= nhentai.get_doujin(id=hid)
    else:
      try:
        hsearch = nhentai.search(query=hid , sort='popular', page=1)
        size = hsearch.total_results
        total = hsearch.total_pages
        Doujin = nhentai.get_doujin(id = hsearch.doujins[random.randint(0,(size-1)//total)].id)
      except:
        await ctx.send("Enter a valid id or search string else leave search field empty ")
    
    if Doujin:
      embed,i= embedDoujin(Doujin,i)
      message = await ctx.send(embed=embed)
      await message.add_reaction(emoji='👈')
      await message.add_reaction(emoji='👉')
      await asyncio.sleep(1)
      loop = True
      while loop:
        try:
          reaction, user = await self.client.wait_for('reaction_add',check=lambda reaction, user: (reaction.emoji == '👉' or reaction.emoji=='👈') and user == ctx.author and reaction.message.id == message.id,timeout= 30.0)
        except:
          loop= False
        else:
          if reaction.emoji =="👉":
            embed,i=embedDoujin(Doujin,i+1)
          else:
            embed,i=embedDoujin(Doujin,i-1)
          await message.edit(embed=embed)
          await message.remove_reaction("👉",ctx.author)
          await message.remove_reaction("👈",ctx.author)

def embedDoujin(Doujin,i):
    i=i%Doujin.total_pages
    embed=discord.Embed(title=Doujin.title,url='https://nhentai.net/g/{0}/'.format(Doujin.id),color=discord.Color.red())
    embed.set_image(url=Doujin.images[i])
    embed.set_footer(text = "Page {0} / {1}".format(i+1,Doujin.total_pages))
    return embed,i



def setup(client):
  client.add_cog(Hentai(client))