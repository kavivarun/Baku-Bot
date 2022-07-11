import os
import discord
from discord.ext import commands
import requests
import json
import random
from PIL import Image

tenorapi = os.environ['TENOR']
#class for any utility related feature.
class Utility(commands.Cog):

  #initializing discord client into class instance
  def __init__(self,client):
    self.client=client

  #command for flipping a coin
  @commands.command(aliases = ["toss","coinflip"])
  async def flip(self,ctx):
    await ctx.send("Heads" if random.randint(1,2)%2==0 else "Tails")

  @commands.command()
  async def ping(self,ctx): 
    if str(ctx.author)=="Lord Explosion Murder#7843":
      await ctx.author.send("Hey Manu, It's been a year since last time. Already a year huh! Well you are 21 one years old now. I find it hard to express my feelings and I am not a particularly good writer but here I go! A lot has changed since last year, I was able to claim a precious girlfriend, We were able to share lots and create lots of memories, We fought , we played , we made love, we did lots of things together. I dont know what the future holds, but I want to steer it towards the direction where I can grow older with you, I hope you have a wonderful year ahead and better ones onward. Here are some of the memories we made last year, I hope to create more fun new ones with my legal wifeable baby!")
      embed=discord.Embed(title="Sri's B'day", description="One of our recent memories. I simply could not stop staring at you. You were looking cuter by the minute and I wanted to devour those lips of yours",color=0xFF5733)
      embed.set_image(url="https://lh3.googleusercontent.com/kBpNLjQAH9oka5VH2sgziFOvhi_vqHaIvhS2t9Xt41H9imC1-vwUELfJPGYuaztTaszvHWBoeI02cZin7evf1qgmRWXy2hxjt6Eu5nRkM6vQ2aTWb6FSTWR4ZZhKu6MRkTE-lfbCcsV9cjhgTjjL33zISWsMFgTFX4anrVPJIv0TWjuvuBLWB9LGdK_M7Qfw9IJKqLqnd9EGBVkj4KJsrCL6kCPAfq753UR5ovR9QwT5wTpaa_zFnSuchl-Csv15PBm4zQVq0TBq1UsbMw1Sf6Y7blWOQ95hLLGUcG9QwWLNfAmXcw34t_ZHu9gVkJ9hRZvVtOnuuWjrwxwwxlanqBqaLRy0iNe_TYbWuKtT-8jyziLc4VhCsUOkBsRU31NBZLljRnQn2bKQLt4TzOr-x8lvC2_Xkk9boY1P0j9tFihDn-bcESomxBTi82tlnqldMsrQn2a0BCUIfI22Zmyuzm3OPMIsbaT_NOnYPlVI3XQuIBQ2iY2ZUn2nGs31vbuK82j9WooMYS7h4bDNNP4D3rsRx8TedBGTqbk5GYvGV8KmnUNEfHAGkZoJg6_0SqxDZ1w2XtUNs2Ojp-OjV2TBEjAe8RGrfDYjncW6TDs8ly_0zGkEmewtbbh7FNAugc5_wqEewHix9geKwFzYk2O3DvR8ptaet4177bfL3tAJK72q3Pcns06ctCDBgRvX9iuwuAQZx-Mo6Nd91GCi8qmWchM6jDpbc9CWWpq2cCndjMKh3K6CsnqLgLIGWBEGDzf2aVfLX0MxEBeTL2WBy9psTSueoXynaOqSG242vAj-MdZw7n6FuYA79Nv99wQkML6DqFnQ18w=w660-h879-no?authuser=0")
      message = await ctx.author.send(embed=embed)
      await message.add_reaction(emoji='❤️')
      embed=discord.Embed(title="Vikram Movie Time", description="Apart from the movie being good, It felt really nice being able to hold you hand and stare at you while you were busy focused on the movie that day. We had nice deserts and had heaps of fun",color=0xFF5733)
      embed.set_image(url="https://lh3.googleusercontent.com/PgxeErgcgLlnLcqTIZT516NaGkxUFWA7fyAzBEL9h31OBLDB7EU7XLo8spugNlfKwfdTC9VYha8EswrhaOCNZcQCLi27htwihdICL6DF6Scwg2cWVx1P5AnmgbS_T2ngvKrc-BSQEoZu11fqOZIGSj1U1COWWwj8kMmoR2a0Fp2B2r1-zhpuU-159aeroQBfSNJstcBFarvCDelaww-vl6LclAdYqTV25DT9rUz8E3ouCRSbylOTLAmN1sp39gzTDf5oQbfryWsNicUiWojEfqBw88a9k7-MRRLyuFXIMDfxU1z76ja4LFw0eFBsVJbdDmwzYg7QwZbAKG-zU1O8k5Rz1t94xQVvf4s08A5yODWCDBzdJS0LeAbxQMwJtCVzuQfdasDjiNEoACJeE0Ma-vBDvLU4Vin21mgU-MdtWGGBBCSp4ocCdt6F-y3pjHneaGz63aKT87U0nMAS-WXYh8whwyxzLSuAUfuBUVGr9T9KHwmqzYnjgwaP0n3Qw67BFkGMOpvtLTLezv-rSuSI5GeSvL1VZtVknk1n-vKlSRkeYwMUkivyn45vdVchsDOiPVBBuT6r4RJHIiRuc7pHdtgstRO1zJaxWswCpUO_OqIoa94L4Tj06CiBvoQhXiPHfk5ByOD97r4DNZitHp1QjwI1KLYZWX8aU2GJ7jkeg7JL_28SwkHcq4DauXsjeu3aTxwDTFrWYhskDyhEwKBzmEMX-ykyUcGI4gxWBSHE5JEHcyRWZzN8F38k2mtsSpCLy9qRNlNf792tohr7-aRLbF9jdsOje6jUHTta2TySJhNSe6XeVa5ClV1tjPMbV8KsALFSrho=w1280-h597-no?authuser=0")
      message = await ctx.author.send(embed=embed)
      await message.add_reaction(emoji='❤️')
      embed=discord.Embed(title="Patissez and Fun City", description="We reached a bit early and sat in a corner, You let me play around with your phone and look at this!! I love this photo. Both of us look really good. Dont we make a good couple!!!",color=0xFF5733)
      embed.set_image(url="https://lh3.googleusercontent.com/_HJf9nzQSfWA7cjikO3PM3MjpHoXr6ta6NgPzNpxqumKnX2xrxsgR5lyTmRv08InHjbtLyfx9c69WlF8Bi5wdSgEd-LV_A8sOjFVmVHldoKmfnijWmIngAL566vz14gMB5StibOJUViE0xyT7W2jsGjY9COXGk811Ya2wgEaQGLlMXdLvMLrXB8-9oHf6eQtgGkJVJrNKT-CzT4drGwpvT-fc-n2nLkZw2MAFfnWvHLPd_fKO_a6_Crg5yZlRNH9B6eoWa4nz7TOkRCXn9Ny8N75WUobYjy2HPWpVpN2pMOBWI7vtVB8QDQDrRYvXEBUlDLe-aBRqPkyZGxylpHW4DwDR5neWcuIFbnFGxekw3vkyL8d_ldvXdf1mZeEt55QJEszBKJ0YaoTDAKc8LcStIXbKUblayb9tRTO4fkLx6GzWNAmBeotuEZIEOMNd11tT4xhxurXPYgRayLlkyRPQJjAoMWq54Xvvf_nZ63c1fX6gTY4YYxTtH1nRH64edS9J_hGFUArOC3olDNlI80gnvrhoxRFoJSRMlRqbHzxh5K8-RpY9ZUILII_zEW5KFBuv_WZ-kVd0Sy1WbyYk0OYnEGXqyKiU2QQOIAqugFlTPTGtMkKXb3Rr2odZpwc3VnCdIWMRCQLSompTjowN0d7ZFgoLZt6IURUNg_7ZaJHFBJCwZYathgOBwv90No0J6Lp8W_rtbycu0eH-HBMWTojPXQi7wjhBFgR3d5s3rm4ESNKcjhkuFhn0AqPlx1JGIKcv_ktfP8cqRQMZnhdrfKFsvPmNEylQRTyW__Z037TDFmvWe9cOY-_apbL2P_BeXgXSWfvkec=w442-h879-no?authuser=0")
      message = await ctx.author.send(embed=embed)
      await message.add_reaction(emoji='❤️')
      
      embed=discord.Embed(title="Patissez and Fun City Contd.", description="All of them came now, We had an amazing day with good food and alot of fun at fun city. You were soo cute when you became catto and I had to move you around",color=0xFF5733)
      embed.set_image(url="https://lh3.googleusercontent.com/ao_jJQDnDMGQ45ASNIqxtLuNHSS9-m7i9b3MkByHARMhvBkvAaKEBPsBDS9ygjwvROTplL4AqNc554T63-_F1jx6EAZQ4gFlVzNGjVGSl3S_c-zmBJ-P8LYCS0uLwq4RFdgZeRRCh7LPI0WRLIiy-RASqqsnkBn4S9uE1mjMB1c_F24PpRbWBGqhkBJXW7Cmo8L4T56ePtNh1xlf0qN98JuTTjVLPMzaHsiIlR9uvU-HGq6HMUnKPimQBun9okE5pW5XM2X3PkTMVos2fpeDaG_JYIFNU57cwt5Hs94qu_vWWj0hF1fQw9VKYQ_90Ozv3B_puWVg5_oN9wEVOsuY-nX8aQtkxhTeFRlVNLsUqFAXcyp1nX7N7sTUr2Xu4PoJa9BurnneyBGFuU7Sf4GQ5bdi5ItvTa6QIYX2C59ZoGto1btolwZwVknyQbwNUkx6pzQhdKrDOLXuEHFoasMu1TaLy7druxINQpb4XHykhvD4SKw8jbgn35JyLdfWwfT-JXZwhd3Ya1PF2nzj1nPYnxqivQp9ByRtAEmtqPdBsnxH7vtPUoolYl9wAoFuJ15qAGcM2wtZ-wmhNj0r59AqkVrIWx_dl30Bv4R_m8PbGjLKWnecxZOcvUTWSsO2FYI6-1Rn0lA2Mb0WOGiIId0dn8ZA5cFt9wduqcuYQqhtQlfhw7t80vTxDyG4LojdQHPieQtwXNHW1E8Kzr-oFF22zJ4omGKAKm3nBMZIoRAZcdMVrE8t9m0E3VUXzw1gaM_Rbah9jUIpFGWMqcbUGQE3YluUXlMTRABpGWvGb2NPIvo3u99kEVyPD1-9FRwXjch2gYEQxOY=w1173-h879-no?authuser=0")
      message = await ctx.author.send(embed=embed)
      await message.add_reaction(emoji='❤️')
      embed=discord.Embed(title="Sangam Cinemas", description="Well... Was a great time wasnt it. The movie yeah! Nice movie for sure... ;)",color=0xFF5733)
      embed.set_image(url="https://lh3.googleusercontent.com/MI3OgbGtdJoisOdLklF-XXfadOpFSPjnwB0NEkEnKwWWtAiKEUJuln-a-hlPw1w2TPXI8KvMj_gIhysjPk6kYK6cIXLegjThr0XaMuhZvBWSWF_DsvuvAN_L6euN1lQYt99GwoZohIZBZkWEBOY7iA2oZLkB7tDs2P-AgfnyeC8HVpOv9o_ZPY2K4IoZEUB7fBk69Dp-2fDjmoWJyzRCzDMB7w9cZMq4t0jSVevL0jzcIm5-oNT4jhHWbFZpWC83UHngwfcrfs3qQOGfo6eACvV9Fr8dVnBpX1kQ4OafsSoGc1dOPICRMlkSG9MEAg6hMc28NQ32oAtFW4nYex_hzH38qks8YpsFsfw2avO3EsWG-K4964Y4j5QYcrXt_3lnwpHY4lUUlBPPfdwOmCRp_BgG2_T-2UjdfIvtaAaSmbx2YUycbeCe1Cumaf08k-zXWeDocvMz4lKDWvpowJTEOVgPAfQdkbkBiMCMx0vgY2GO1O-K0HxCpHKLxjNCqJw8WWiOJxJHAypJDtDUOycdTkxUGcZEOuWk3nXOJMO1rKk5KQGFkTMnFD3FDiGfuv1xY2egi2BBDZPo9tjmc2lfPmgNyIgX_hfITb8RBontYZO4ItNtnPcIArD9u6CCNZyRIlCXm3IeSkwniu8uIp0b4HrbhBFiMWBmgL8z3qHVA83fyybKaigERLAaFWTdJuPEpPhvsPO-WdaXzk1fU-hw6oGBcTxt2bbXPCTIuDcsLFB_RZ0mJ3edCQ8GF-FHi5Qux_ckSaSk_UOoECh_ggtHFSO3qap57WAP393iDJDDLkfpdWl_uVfROR_pWvBzTWRBdfgx3j8=w439-h950-no?authuser=0")
      message = await ctx.author.send(embed=embed)
      await message.add_reaction(emoji='❤️')
      embed=discord.Embed(title="What will I do Without you?", description="Cross your heart and tell me this is not cute. I'll give you as much hugs as you want.",color=0xFF5733)
      embed.set_image(url="https://lh3.googleusercontent.com/V42wa6SB2z4OP8V_ViExS4fZSfWvD2o2xe0UboCv2OutKlZgFGimU5aTsZ-H2rijSovEYjv-sUmcK-3JWEiZBH-syMbIZDOqUQO3pDsBvbOFYDP1HoxSQqRcMLzltI-puUZCT6xKBlkS7FXV-fYAW5mdyzmp2pJnQUdR3BEyTfNqeJcpKJNLLn4lCF2jLewWWSUavqntwpqAv4xiy5MW251UPHQtRjDu_0LaZRMvKEia_SHBQKws7h421SwIt_6zG21R364QE_OOIOcerDZimrZ50Dwn9xTPPhoq_HN-tsBDSKHANddN4vwKXIQlfeR7oZ3KKzJMbzheI2cMW6lnQSt2m5DmJdk7HxHkgQwe4KhB460RhJL_BEDQa5T4BEpyrlTXNzPXKBDUd5pqlNjuJ085Lk4G2dmGzqgVrtQtP-fxixQDUzUanzXRT7Q23NLav97h9BN030M6X_PIX9k49g39OzBZf13b-8KPNGY9jRYF4f3iMZQIxxCAl6QpB1JRzhJ36_o4XK30yf4f6ujz-mf9FXNKcVxxyNIOKCl9JvKS1mqPMR9xedn6aZWCNsqRhsOUejHonZ8AVpUtiROQfYk1SgAW-IiNWKmupT5TAN2eyF48OvhRpiKH5qiZqlrRyF4WWu1eU4ndb0ZepvHqEheQMtRfGWyA5qitYA1-1V0gvC6MTf4nq_EwNgDDRgTnyuFa8SsP9GkwmoT-iSPTZDWOJbM6heeuKu3j0oYQfhafIUbGHa3mruJIVf_Mb0dlDMk-lawRjyKFb3tbBgR01P1xf7Dfh7lDXQWf7FWee1tYepvWUWRAeZ-t2rXUVZhJ062aJsU=w438-h879-no?authuser=0")
      message = await ctx.author.send(embed=embed)
      await message.add_reaction(emoji='❤️')
    else:
      await ctx.author.send("Pong!")
    
  @commands.command(aliases=["g","GIF","gifs"])
  async def gif(self,ctx,*,search):
    g=gifs(search,tenorapi,50)
    if g == None:
      await ctx.send("Error finding gifs at this time, Try again")
    else:
      embed=discord.Embed(title="here you go",color=discord.Color.red())
      embed.set_image(url=g['results'][random.randint(0,51)]['media'][0]['gif']['url'])
      embed.set_footer(text ="Gifs supplied by Tenor")
      await ctx.send(embed=embed)


def gifs(search,api,limit=50):
  r = requests.get("https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, api, limit))
  if r.status_code == 200:
    # load the GIFs using the urls for the smaller GIF sizes
    gifs = json.loads(r.content)
    print()
  else:
    gifs = None
  return gifs

#setting up all the cogs(functions) 
def setup(client):
  client.add_cog(Utility(client)) 