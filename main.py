import discord
import os
from prays import pray
import requests
import json
import random
from discord.ext import commands
from replit import db
import praw
from auto_run import keep_alive

my_secret = os.environ['ToKen']

client = commands.Bot(command_prefix = 'r')

def get_meme():
  response = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
  res = response.json()
  joke = res["joke"]
  category = res["category"]
  beep = res["joke"];
  return(beep)

reddit = praw.Reddit(client_id = "2pLCj-SbyVDeLLo-qTW5NA", 
client_secret = "3wRDy9JpMc-IEtc1YL3OCxKKRt_m_Q",
username = "subodh_c137",
password = "wtfbruh69",
user_agent = "reefer")


@client.command()
async def thighs(ctx):

  await ctx.send(embed = em)


@client.event
async def on_ready():
  print("Reef is Ready")

client.count = 0
client.count1 = 0
@client.event
async def on_message(message):
  if message.content.lower() == 't6troll':
    client.count = client.count + 1
    embed=discord.Embed(title="Fuyumi and Staz", color=0xff0000)
    embed.set_image(url= "https://media.discordapp.net/attachments/900288270674591774/900574722260103218/Anime_Soul-718467435086217297-900288270674591774-claim-drop.png")
    embed.description= "To claim, use claim [captcha code]\nSee your card inventory on our site.\nSupport us and get global rewards!\nClaim exclusive MHA Cards!"
    embed.set_footer(text="Powered by AS Devs"
     )
    await message.channel.send(embed=embed)
  if message.content.lower() == 't6pray':
    client.count = client.count + 1
    embed=discord.Embed(title=f"{message.author}You are praying for a T6", color=0xd1a1e8)
    embed.set_image(url= random.choice(pray))
    embed.set_footer(text="Users have prayed for a T6 on this server "+str(client.count)+" times !" )
    await message.channel.send(embed=embed)
  if message.content.lower() == 'droppray':
    client.count1 = client.count1 + 1
    embed=discord.Embed(title=f'{message.author} is praying for a pog drop.', color=0xd1a1e8)
    embed.set_image(url= random.choice(pray))
    embed.set_footer(text="Users have prayed for a pog drop on this server "+str(client.count1)+" times !" )
    await message.channel.send(embed=embed)
  if message.content.lower() == ";ping":
    if((round(client.latency*1000))<60):
      await message.channel.send(f'The pong took {round(client.latency * 1000)}ms! \nNice wifi bruhh.')
    else:
      await message.channel.send(f'The pong took {round(client.latency * 1000)}ms! \nUpgrade wifi when?.')
  if message.content.lower().startswith('joke'):
    meme = get_meme()
    await message.channel.send(meme)
  if message.content.startswith('8ball'):
    responses = ['Bruhh.. Lmao', 'Man I dunno', 'Maybe Not ?', 'You seriously asking me this ?', 'I am a bot bro.. ask real hooman when ?','Ask that to the FBI','The real question is \"why?\"','I\'m just an 8ball bro.. leave me outta this ;-;','Do you even know how stupid it sounds?','Yes hoe-mie of course!','No lol']
    await message.channel.send(f'{random.choice(responses)}')
  if message.content.lower().startswith('thii'):
    subreddit = reddit.subreddit("memes")
    allsub = []
    top = subreddit.top(limit = 5)

    for submission in top:
      allsub.append(submission)
  
    ransub = random.choice(allsub)
    namee = ransub.title
    urll = ransub.url

    em = discord.Embed(title = namee)
    em.add_image(url = urll)    
    await message.channel.send(embed=em)




keep_alive()
client.run(my_secret) 