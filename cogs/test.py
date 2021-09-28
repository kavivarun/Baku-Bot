import discord
from discord.ext import commands
from discord_components import Button, Select, SelectOption, ComponentsBot

class Test(commands.Cog):
  def __init__(self,client):
    self.client=client

  @commands.command()
  async def button(self,ctx):
    await ctx.send("Buttons!", components=[Button(label="Button", custom_id="button1")])
    interaction = await self.client.wait_for(
        "button_click", check=lambda inter: inter.custom_id == "button1"
    )
    await interaction.send(content="Button Clicked")

  @commands.command()
  async def select(self,ctx):
    await ctx.send("Selects!",components=[Select(placeholder="Select something!",options=[SelectOption(label="a", value="a"),SelectOption(label="b", value="b"),],custom_id="select1",)],)
    interaction = await self.client.wait_for(
          "select_option", check=lambda inter: inter.custom_id == "select1"
      )
    await interaction.send(content=f"{interaction.values[0]} selected!")

def setup(client):
  client.add_cog(Test(client))