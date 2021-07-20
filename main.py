import discord
from discord.ext import commands
import os
import random
from NHentai.nhentai import NHentai
from keep_alive import keep_alive

client = discord.Client()
client = commands.Bot(command_prefix="baku ")
nhentai = NHentai()

@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))

@client.command()
async def sauce(ctx,*,search=""):
    if search == "":
      Doujin = nhentai.get_random()
    elif search =="popular":
      popular = nhentai.get_popular_now()
      Doujin =nhentai.get_doujin(id=popular.doujins[random.randint(0,popular.total_doujins-1)].id )
    else:
      hsearch = nhentai.search(query=search , sort='popular', page=1)
      size = hsearch.total_results
      total = hsearch.total_pages
      Doujin = nhentai.get_doujin(id = hsearch.doujins[random.randint(0,(size-1)//total)].id) 
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
async def _read(ctx,*,hid):
  Doujin = 0
  i=0
  print(hid)
  if hid.lower().startswith('random'):
    Doujin = nhentai.get_random()
  elif len(str(hid))==6 and str(hid).isdigit():
    Doujin= nhentai.get_doujin(id=hid)
  print(Doujin)
  if Doujin == 0 or None:
    await ctx.send("Enter a Valid id or 'random' ")
  else:
    embed=discord.Embed(title=Doujin.title,url='https://nhentai.net/g/{0}/'.format(Doujin.id),color=discord.Color.red())
    embed.set_image(url=Doujin.images[i])
    embed.set_footer(text = "Page {0} / {1}".format(i+1,Doujin.total_pages))
    message = await ctx.send(embed=embed)
    await message.add_reaction(emoji='👈')
    await message.add_reaction(emoji='👉')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)

keep_alive()
client.run(os.getenv('TOKEN'))  