import discord
from discord.ext import commands
from random_word import RandomWords

r = RandomWords()

class Games(commands.Cog):
  def __init__(self,client):
    self.client=client
  
  #command for playing hangman
  @commands.command()
  async def hangman(self,ctx):
    word=r.get_random_word(hasDictionaryDef="true",maxDictionaryCount=10, minLength=6, maxLength=12)
    word=word.lower()
    loop = True
    guessed_chars=[]
    img=["","https://i.imgur.com/hRzVg1N.png","https://i.imgur.com/cQmLMDO.png","https://i.imgur.com/sAeTvqP.png","https://i.imgur.com/yHGrZqc.png","https://i.imgur.com/UKiV6J9.png","https://i.imgur.com/w7QJQFH.png","https://i.imgur.com/KBMsCp9.png","https://media1.tenor.com/images/cb6eed2a7e9fb73f44d53f93ffe92c9c/tenor.gif"]
    chance=0
    while loop:
      if chance == 0:
        embed=discord.Embed(title="Hangman",description="A word guessing game where the player attempts to build a missing word by guessing one letter at a time or the word as a whole.After a certain number of incorrect guesses, the game ends and the player loses. The game also ends if the player correctly identifies all the letters of the missing word. There are only lowercase letters and '-' ",color=discord.Color.blue())
        embed.set_image(url=img[1])
        embed.add_field(name=printWord(word,guessed_chars),value="\nThe word had {0} characters".format(len(word)),inline=False)
        embed.set_footer(text="Good luck ")
        message = await ctx.send(embed=embed)
        chance+=1
      try:
        msg = await self.client.wait_for('message',check=lambda msg: msg.author == ctx.author,timeout= 20.0)
      except:
        loop= False
        embed=discord.Embed(title="User failed to respond, Game Over",color=discord.Color.red())
        embed.set_image(url=img[-2])
        await message.edit(embed = embed)
      else:
        if word==msg.content:
          embed=discord.Embed(title="You got the word right!!",description ="It was "+ word,color=discord.Color.green())
          embed.set_image(url=img[-1])
          await message.edit(embed=embed)
          await msg.delete()
          break
        if len(msg.content)==1 and msg.content not in guessed_chars and msg.content in word:
          guessed_chars.append(msg.content)
          if len(set([i for i in word]))==len(guessed_chars):
            embed=discord.Embed(title="You guessed all the characters!!", description="the word was "+word,color=discord.Color.green())
            embed.set_image(url=img[-1])
            await message.edit(embed=embed)
            await msg.delete()
            break
          else:
            embed=discord.Embed(title="Hangman",color=discord.Color.blue())
            embed.set_image(url=img[chance])
            embed.add_field(name=printWord(word,guessed_chars),value="\nGood Work! The letter exists.",inline=False)
            embed.set_footer(text="There were {0} instances of the character {1}".format(word.count(msg.content),msg.content))
            await message.edit(embed=embed)
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
        if chance>6:
          embed=discord.Embed(title="Game Over",description = "The word was "+ word,color=discord.Color.red())
          embed.set_image(url=img[-2])
          await message.edit(embed=embed)
          await msg.delete()
          break
        await msg.delete()


def printWord(word,chars):
  s=""
  for i in word:
    if i in chars:
      s+=i+" "
    else:
      s+="‗ "
  return s

def setup(client):
  client.add_cog(Games(client))