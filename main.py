import discord
from discord.ext import commands
import os
import random
from NHentai.nhentai import NHentai
from keep_alive import keep_alive
import asyncio

client = discord.Client()
client = commands.Bot(command_prefix="baku ")
nhentai = NHentai()

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online,activity= discord.Game("The Sauce Finder"))
  print('logged in as {0.user}'.format(client))

@client.command(aliases = ["sauce"])
async def _sauce(ctx,*,hid=""):
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

@client.command(aliases = ["flip","toss","coinflip"])
async def _flip(ctx):
  await ctx.send("Heads" if random.randint(1,2)%2==0 else "Tails")

@client.command(aliases = ["read"])
async def _read(ctx,*,hid=""):
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
        reaction, user = await client.wait_for('reaction_add',check=lambda reaction, user: reaction.emoji == '👉' or '👈' and user == ctx.author,timeout= 30.0)
      except:
        loop= False
      else:
        if reaction.message.id == message.id:
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
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)

keep_alive()
client.run(os.getenv('TOKEN'))  