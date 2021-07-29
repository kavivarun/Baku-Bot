import os
import discord
from discord.ext import commands
import random
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw 

#class for all meme related commands
class Memes(commands.Cog):

  #initializing discord client to instance client
  def __init__(self,client):
    self.client = client

  @commands.command(aliases=["Monke","MONKE"])
  async def monke(self,ctx,*,text):
    #urllib.request.urlretrieve("https://i.imgflip.com/57cc98.jpg", "monke.jpg")
    img=Image.open("./images/monke.jpg")
    title_text = text
    image_editable = ImageDraw.Draw(img)
    font = ImageFont.truetype(font="./fonts/NotoEmoji-Regular.ttf",size=20)
    image_editable.text((350,20), title_text, (0, 0, 0),font=font)
    with BytesIO() as image_binary:
      img.save(image_binary, 'PNG')
      image_binary.seek(0)
      await ctx.channel.send(file=discord.File(fp=image_binary, filename='image.png'))
def setup(client):
  client.add_cog(Memes(client))