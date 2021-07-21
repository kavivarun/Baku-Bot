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
    loop = True
    guessed_chars=[]
    img=[]
    chance=0
    while loop:
      if chance == 0:
        chance+=1
        embed=discord.Embed(title="Hangman",color=discord.Color.blue())
        embed.add_field(name=printWord(word,guessed_chars),value=word,inline=False)
        message = await ctx.send(embed=embed)
      try:
        msg = await self.client.wait_for('message',check=lambda msg: msg.author == ctx.author,timeout= 15.0)
      except:
        loop= False
        embed=discord.Embed(title="User failed to respond, Game Over",color=discord.Color.red())
        await message.edit(embed = embed)
      else:
        if word==msg.content:
          embed=discord.Embed(title="You got the word right!!",description ="It was "+ word,color=discord.Color.green())
          await message.edit(embed=embed)
          await msg.delete()
          break
        if len(msg.content)==1 and msg.content not in guessed_chars and msg.content in word:
          guessed_chars.append(msg.content)
          if len(set([i for i in word]))==len(guessed_chars):
            embed=discord.Embed(title="You guessed all the characters!!", description="the word was "+word,color=discord.Color.green())
            await message.edit(embed=embed)
            await msg.delete()
            break
          else:
            embed=discord.Embed(title="Hangman",color=discord.Color.blue())
            embed.add_field(name=printWord(word,guessed_chars),value="\nGood Work! The letter exists.",inline=False)
            embed.set_footer(text="There were {0} instances of the character {1}".format(word.count(msg.content),msg.content))
            await message.edit(embed=embed)
        else:
          chance+=1
          embed=discord.Embed(title="Hangman",color=discord.Color.blue())
          embed.add_field(name=printWord(word,guessed_chars),value="\nWrong Guess !!",inline=False)
          embed.set_footer(text="There were no instances of the character {0}".format(msg.content))
          await message.edit(embed=embed)
        if chance>=6:
          embed=discord.Embed(title="Game Over",description = "The word was "+ word,color=discord.Color.red())
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