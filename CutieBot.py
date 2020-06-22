# aqua.py
# https://discord.com/api/oauth2/authorize?client_id=724544193489272842&permissions=8&scope=bot

import discord
from data import compliments
from discord.ext import commands
from dotenv import load_dotenv  # load module for usage of a .env file
import os  # import module for directory management
import random

# discord token is stored in a .env file in the same directory as the bot
load_dotenv()  # load the .env file containing id's that have to be kept secret for security
TOKEN = os.getenv('DISCORD_TOKEN')  # get our discord bot token from .env

bot = commands.Bot(command_prefix='qt!')

fubyID = 724544193489272842


@bot.event
async def on_ready():
    print('bot connected')
    await bot.change_presence(activity=discord.Game("Being Gay"))


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            greeting = "Hello, Welcome to the greatest server of all time"
            await channel.send(greeting)


@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return

    if bot.get_user(fubyID) in message.mentions:
        response = "Hi, I'm Fuby and I'm cute!"
        await message.channel.send(response, delete_after=60)

    if "iron forge" in message.content:
        response = "that's a trash upgrade"
        await message.channel.send(response)

    await bot.process_commands(message)


@bot.command(name='test', help='test if the bot is working')
async def test(ctx):
    response = 'Don\'t worry, I\'m working!'
    await ctx.send(response)


@bot.command(name='compliment', help='admire fuby randomly')
async def compliment(ctx):
    response = random.choice(compliments)
    await ctx.send(response)


bot.run(TOKEN)
