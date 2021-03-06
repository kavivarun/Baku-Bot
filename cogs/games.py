import discord
from discord.ext import commands
import subprocess
import sys

try:
  from random_word import RandomWords
except ImportError:
  subprocess.check_call([sys.executable, "-m", "pip", "install", "pyyaml"])
  from random_word import RandomWords

#Loading Random word api
r = RandomWords()

currently_running=[]

#class for all commands related to hentai
class Games(commands.Cog):
  
  #initializing discord client into class instance
  def __init__(self,client):
    self.client=client
  
  #command for displaying rules of hangman
  @commands.command(aliases=["HANGMANRULE","hr","HR"])
  async def hangmanrule(self,ctx):
     embed=discord.Embed(title="Hangman",description="A word guessing game where the player attempts to build a missing word by guessing one letter at a time or the word as a whole.After a certain number of incorrect guesses, the game ends and the player loses. The game also ends if the player correctly identifies all the letters of the missing word. There are only lowercase letters and '-' ",color=discord.Color.red())
     embed.set_thumbnail(url="https://i.imgur.com/KBMsCp9.png")
     await ctx.send(embed=embed)


  #command for playing hangman
  @commands.command(aliases =["hm","HANGMAN"])
  async def hangman(self,ctx):
    channel_id = ctx.message.channel.id
    if channel_id in currently_running:
      await ctx.send("Only one instance of hangman can be run in a Channel")
    else:
      currently_running.append(channel_id)
      #getting a random word from the API
      try:
        word=r.get_random_word(hasDictionaryDef="true", minCorpusCount=5,minLength=6, maxLength=12)
        word=word.lower()
      except:
        await ctx.send("There was a problem with creating game, Try again.")
        currently_running.remove(channel_id)
      
      #base variables
      loop = True
      guessed_chars=[]
      chance=0

      #URL list for hangman images
      img=["","https://i.imgur.com/hRzVg1N.png","https://i.imgur.com/cQmLMDO.png","https://i.imgur.com/sAeTvqP.png","https://i.imgur.com/yHGrZqc.png","https://i.imgur.com/UKiV6J9.png","https://i.imgur.com/w7QJQFH.png","https://i.imgur.com/KBMsCp9.png","https://media1.tenor.com/images/cb6eed2a7e9fb73f44d53f93ffe92c9c/tenor.gif"]
      
      #Loop for Game Logic
      while loop and word:

        #Initial embed
        if chance == 0:
          embed=discord.Embed(title="Hangman",description="Game started by {0}. Type 'baku hr' to learn how to play".format(ctx.message.author),color=discord.Color.blue())
          embed.set_image(url=img[1])
          embed.add_field(name=printWord(word,guessed_chars),value="\nThe word had {0} characters".format(len(word)),inline=False)
          embed.set_footer(text="Good luck {0}".format(ctx.message.author))
          message = await ctx.send(embed=embed)
          chance+=1
        #Waiting for user response
        try:
          msg = await self.client.wait_for('message',check=lambda msg: msg.author == ctx.author and msg.channel.id == channel_id,timeout= 20.0)
        except: #Exit on no reply
          loop= False
          embed=discord.Embed(title="{0} failed to respond, Game Over".format(ctx.message.author),color=discord.Color.red())
          embed.set_image(url=img[-2])
          embed.set_footer(text="The word was "+ word)
          await message.edit(embed = embed)
          currently_running.remove(channel_id)
        else: #Game Logic processing on reply
          if word==msg.content.lower(): #Word guessed properly
            embed=discord.Embed(title="You got the word right!!",description ="It was "+ word,color=discord.Color.green())
            embed.set_footer(text="Good Job {0}".format(ctx.message.author))
            embed.set_image(url=img[-1])
            await message.edit(embed=embed)
            await msg.delete()
            currently_running.remove(channel_id)
            break
          if len(msg.content.lower())==1 and msg.content.lower() not in guessed_chars and msg.content.lower() in word: #Character guessed properly
            guessed_chars.append(msg.content.lower())

            #Word guessed by finding all characters
            if len(set([i for i in word]))==len(guessed_chars):
              embed=discord.Embed(title="You guessed all the characters!!", description="the word was "+word,color=discord.Color.green())
              embed.set_footer(text="Good Job {0}".format(ctx.message.author))
              embed.set_image(url=img[-1])
              await message.edit(embed=embed)
              await msg.delete()
              currently_running.remove(channel_id)
              break
            #Character guessed exisits in the word
            else:
              embed=discord.Embed(title="Hangman",color=discord.Color.blue())
              embed.set_image(url=img[chance])
              embed.add_field(name=printWord(word,guessed_chars),value="\nGood Work! The letter exists.",inline=False)
              embed.set_footer(text="There were {0} instances of the character {1}".format(word.count(msg.content.lower()),msg.content.lower()))
              await message.edit(embed=embed)
          #character guessed does not exisit in the word
          else:
            chance+=1
            embed=discord.Embed(title="Hangman",color=discord.Color.blue())
            embed.set_image(url=img[chance])
            embed.add_field(name=printWord(word,guessed_chars),value="\nWrong Guess !!",inline=False)
            if len(msg.content)==1:
              embed.set_footer(text="There were no instances of the character {0}".format(msg.content.lower()))
            else:
              embed.set_footer(text="The word is not {0}".format(msg.content))
            await message.edit(embed=embed)
          if chance>6: #GAME OVER
            embed=discord.Embed(title="Game Over",description = "The word was "+ word,color=discord.Color.red())
            embed.set_image(url=img[-2])
            embed.set_footer(text="Better luck next time {0}".format(ctx.message.author))
            await message.edit(embed=embed)
            await msg.delete()
            currently_running.remove(channel_id)
            break
          await msg.delete()
  
  

#Function for printing identified and unidentified characters
def printWord(word,chars):
  s=""
  for i in word:
    if i in chars:
      s+=i+" "
    else:
      s+="??? "
  return s

#setting up all the cogs(functions) 
def setup(client):
  client.add_cog(Games(client))