import discord
import os
import random
from NHentai.nhentai import NHentai
from keep_alive import keep_alive



client = discord.Client()
nhentai = NHentai()

@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if (len(message.attachments) > 0):
      for i in message.attachments:
        await message.channel.send(i.url)
  
    if message.content.startswith('baku who is gay'):
        await message.channel.send("mulikan is gay")
    
    if message.content.startswith('baku toss'):
        await message.channel.send("Heads" if random.randint(1,2)%2==0 else "Tails")

    
    
    if message.content == 'baku sauce':
      Doujin = nhentai.get_random()
      embed=discord.Embed(title=Doujin.title,url='https://nhentai.net/g/{0}/'.format(Doujin.id),description=str(Doujin.total_pages)+ " Pages",color=discord.Color.red())
      embed.add_field(name="**Tags**",value="`"+"` `".join (Doujin.tags)+'`',inline=True)
      embed.set_footer(text='Artists: {0}'.format(", ".join(Doujin.artists) if len(Doujin.artists)>0 else "Unknown"))
      embed.set_thumbnail(url=Doujin.images[0])
      await message.channel.send(embed=embed)


keep_alive()
client.run(os.getenv('TOKEN'))  