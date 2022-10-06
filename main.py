import discord
from discord.ext.commands import Bot
from replit import db
import os

intents = discord.Intents.all()
bot = Bot(command_prefix="!",intents=intents)

@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.online)

@bot.command()
async def info(ctx,type: str):
  if type.upper() == "BOT":
    Name = bot.application.name
    Icon = bot.application.icon.url
    Owner = bot.application.owner
    Servers = bot.guilds
    Version = os.environ['VERSION']
    Time_Stamp = 
    Raw_Footer = "Info fetched at: {}"
    Footer = Raw_Footer.format(Time_Stamp)
    Info = discord.Embed()
    Info.title = "Bot Info"
    Info.description = ":copyright: PositiveCafe"
    Info.set_author(name=Name,url=None,icon_url=Icon)
    Info.set_footer(text=Footer)
    await ctx.send(embed=Info)
    
    

bot.run("MTAxOTQyMjQ4NTA4MDQ1NzM3Nw.G4rqA-.cCkUdkDiUX_VJw9OewdYZtqwW9YNntot_BnPi8")