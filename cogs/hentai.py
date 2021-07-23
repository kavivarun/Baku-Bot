import discord
from discord.ext import commands
import os
import random
import subprocess
import sys
import asyncio
try:
  from NHentai.nhentai import NHentai
except ImportError:
  subprocess.check_call([sys.executable, "-m", "pip", "install", "NHentai-API"])
  from NHentai.nhentai import NHentai
  
#Loading NHentai-API
nhentai = NHentai()

#class for all commands related to hentai
class Hentai(commands.Cog):


  #initializing discord client into class instance
  def __init__(self,client):
    self.client = client

  #command for getting details of a hentai and displaying it
  @commands.command()
  async def sauce(self,ctx,*,hid=""):
    if ctx.channel.is_nsfw():
      Doujin = 0
      i=0
      #searching and quereying Doujins based on id or search term
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

      #Displaying embed if Doujin exists
      if Doujin:
        embed=discord.Embed(title=Doujin.title,url='https://nhentai.net/g/{0}/'.format(Doujin.id),description=str(Doujin.total_pages)+ " Pages",color=discord.Color.red())
        embed.add_field(name="**Id**\n",value=Doujin.id+"\n",inline=True)
        embed.add_field(name="**Tags**",value="`"+"` `".join (Doujin.tags)+'`',inline=False)
        embed.set_footer(text='Artists: {0}'.format(", ".join(Doujin.artists) if len(Doujin.artists)>0 else "Unknown"))
        embed.set_thumbnail(url=Doujin.images[0])
        message = await ctx.send(embed=embed)
        await message.add_reaction(emoji='📖')
        await message.add_reaction(emoji='❌')
        
        #Waiting for user react input (Timeout in 30 seconds)
        try:
            reaction, user = await self.client.wait_for('reaction_add',check=lambda reaction, user: (reaction.emoji == '📖' or reaction.emoji=='❌') and user == ctx.author and reaction.message.id == message.id,timeout= 30.0)
        except:
            pass
        else:
          if reaction.emoji=="❌":
            await message.delete()
            await ctx.message.delete()
          else:
            await message.delete()
            await ctx.invoke(self.client.get_command('read'),hid=str(Doujin.id))
    else:
      await ctx.send("This command can only be used in a NSFW channel")
  
  
  #command for displaying hentai in a readable format
  @commands.command()
  async def read(self,ctx,*,hid=""):
    if ctx.channel.is_nsfw():
      Doujin = 0
      i=0
      
      #searching and quereying Doujins based on id or search term
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
        
      #Displays embed and reaction if doujin found
      if Doujin:
        embed,i= embedDoujin(Doujin,i)
        message = await ctx.send(embed=embed)
        await message.add_reaction(emoji='👈')
        await message.add_reaction(emoji='👉')
        await message.add_reaction(emoji='❌')
        await asyncio.sleep(1)
        loop = True

        #Waiting for user react input (Timeout in 30 seconds) Loops if reaction confirmed
        while loop:
          try:
            reaction, user = await self.client.wait_for('reaction_add',check=lambda reaction, user: (reaction.emoji == '👉' or reaction.emoji=='👈' or reaction.emoji=='❌') and user == ctx.author and reaction.message.id == message.id,timeout= 30.0)
          except:
            loop= False
          else:
            if reaction.emoji=="❌":
              await message.delete()
              await ctx.message.delete()
            else:
              if reaction.emoji =="👉":
                embed,i=embedDoujin(Doujin,i+1)
              else:
                embed,i=embedDoujin(Doujin,i-1)
              await message.edit(embed=embed)
              await message.remove_reaction("👉",ctx.author)
              await message.remove_reaction("👈",ctx.author)
    else:
      await ctx.send("This command can only be used in a NSFW channel")
'''
  @commands.command()
  async def saucedm(self,ctx,*,hid=""):
    Doujin = 0
    i=0
    #searching and quereying Doujins based on id or search term
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

    #Displaying embed if Doujin exists
    if Doujin:
      embed=discord.Embed(title=Doujin.title,url='https://nhentai.net/g/{0}/'.format(Doujin.id),description=str(Doujin.total_pages)+ " Pages",color=discord.Color.red())
      embed.add_field(name="**Id**\n",value=Doujin.id+"\n",inline=True)
      embed.add_field(name="**Tags**",value="`"+"` `".join (Doujin.tags)+'`',inline=False)
      embed.set_footer(text='Artists: {0}'.format(", ".join(Doujin.artists) if len(Doujin.artists)>0 else "Unknown"))
      embed.set_thumbnail(url=Doujin.images[0])
      message = await ctx.author.send(embed=embed)
      await message.add_reaction(emoji='📖')
      await message.add_reaction(emoji='❌')
      try:
        #reaction , user = await self.client.wait_for('reaction_add',check=lambda reaction: (reaction.emoji == '📖' or reaction.emoji=='❌') and reaction.message.id == message.id,timeout= 30.0)
         msg = await self.client.wait_for('message',check=lambda msg: msg.author == ctx.author and msg.channel.id == channel_id,timeout= 20.0)
      except:
          pass
      else:
        if msg.content=="hi":
          print("hi")
          await message.delete()
        else:
          await message.delete()
          #await ctx.invoke(self.client.get_command('read'),hid=str(Doujin.id))  
'''

#Function for embedding the returned details from nhentai api for read command
def embedDoujin(Doujin,i):
    i=i%Doujin.total_pages
    embed=discord.Embed(title=Doujin.title,url='https://nhentai.net/g/{0}/'.format(Doujin.id),color=discord.Color.red())
    embed.set_image(url=Doujin.images[i])
    embed.set_footer(text = "Page {0} / {1}".format(i+1,Doujin.total_pages))
    return embed,i


#setting up all the cogs(functions) 
def setup(client):
  client.add_cog(Hentai(client))