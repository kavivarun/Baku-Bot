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

#class for all commands related to hentai
class Games(commands.Cog):
  
  #initializing discord client into class instance
  def __init__(self,client):
    self.client=client
  
  #command for playing hangman
  @commands.command()
  async def hangman(self,ctx):

    #getting a random word from the API
    word=r.get_random_word(hasDictionaryDef="true",maxDictionaryCount=10, minLength=6, maxLength=12)
    word=word.lower()
    
    #base variables
    loop = True
    guessed_chars=[]
    chance=0

    #URL list for hangman images
    img=["","https://i.imgur.com/hRzVg1N.png","https://i.imgur.com/cQmLMDO.png","https://i.imgur.com/sAeTvqP.png","https://i.imgur.com/yHGrZqc.png","https://i.imgur.com/UKiV6J9.png","https://i.imgur.com/w7QJQFH.png","https://i.imgur.com/KBMsCp9.png","https://media1.tenor.com/images/cb6eed2a7e9fb73f44d53f93ffe92c9c/tenor.gif"]
    
    #Loop for Game Logic
    while loop:

      #Initial embed
      if chance == 0:
        embed=discord.Embed(title="Hangman",description="A word guessing game where the player attempts to build a missing word by guessing one letter at a time or the word as a whole.After a certain number of incorrect guesses, the game ends and the player loses. The game also ends if the player correctly identifies all the letters of the missing word. There are only lowercase letters and '-' ",color=discord.Color.blue())
        embed.set_image(url=img[1])
        embed.add_field(name=printWord(word,guessed_chars),value="\nThe word had {0} characters".format(len(word)),inline=False)
        embed.set_footer(text="Good luck ")
        message = await ctx.send(embed=embed)
        chance+=1
      
      #Waiting for user response
      try:
        msg = await self.client.wait_for('message',check=lambda msg: msg.author == ctx.author,timeout= 20.0)
      except: #Exit on no reply
        loop= False
        embed=discord.Embed(title="User failed to respond, Game Over",color=discord.Color.red())
        embed.set_image(url=img[-2])
        await message.edit(embed = embed)
      else: #Game Logic processing on reply
        if word==msg.content: #Word guessed properly
          embed=discord.Embed(title="You got the word right!!",description ="It was "+ word,color=discord.Color.green())
          embed.set_image(url=img[-1])
          await message.edit(embed=embed)
          await msg.delete()
          break
        if len(msg.content)==1 and msg.content not in guessed_chars and msg.content in word: #Character guessed properly
          guessed_chars.append(msg.content)

          #Word guessed by finding all characters
          if len(set([i for i in word]))==len(guessed_chars):
            embed=discord.Embed(title="You guessed all the characters!!", description="the word was "+word,color=discord.Color.green())
            embed.set_image(url=img[-1])
            await message.edit(embed=embed)
            await msg.delete()
            break
          #Character guessed exisits in the word
          else:
            embed=discord.Embed(title="Hangman",color=discord.Color.blue())
            embed.set_image(url=img[chance])
            embed.add_field(name=printWord(word,guessed_chars),value="\nGood Work! The letter exists.",inline=False)
            embed.set_footer(text="There were {0} instances of the character {1}".format(word.count(msg.content),msg.content))
            await message.edit(embed=embed)
        #character guessed does not exisit in the word
        else:
          chance+=1
          embed=discord.Embed(title="Hangman",color=discord.Color.blue())
          embed.set_image(url=img[chance])
          embed.add_field(name=printWord(word,guessed_chars),value="\nWrong Guess !!",inline=False)
          if len(msg.content)==1:
            embed.set_footer(text="There were no instances of the character {0}".format(msg.content))
          else:
            embed.set_footer(text="The word is not {0}".format(msg.content))
          await message.edit(embed=embed)
        if chance>6: #GAME OVER
          embed=discord.Embed(title="Game Over",description = "The word was "+ word,color=discord.Color.red())
          embed.set_image(url=img[-2])
          await message.edit(embed=embed)
          await msg.delete()
          break
        await msg.delete()

#Function for printing identified and unidentified characters
def printWord(word,chars):
  s=""
  for i in word:
    if i in chars:
      s+=i+" "
    else:
      s+="‗ "
  return s

#setting up all the cogs(functions) 
def setup(client):
  client.add_cog(Games(client))