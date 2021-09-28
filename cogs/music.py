import discord
import os
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get
import asyncio


FFMPEG_PATH="/home/runner/Baku-Bot/node_modules/ffmpeg-static/ffmpeg"
class Music(commands.Cog):

  def __init__(self,client):
    self.client=client

  @commands.command()
  async def roll(self,ctx):
    # grab the user who sent the command
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(self.client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('./music/roll.mp3')
    player = voice.play(source)
    

def setup(client):
  client.add_cog(Music(client)) 