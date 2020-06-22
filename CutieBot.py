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

# bot prefix for command set to
bot = commands.Bot(command_prefix=('qt!', 'Qt!'))

fubyID = 724544193489272842


# print a message if the bot is running
# change bot status to playing the game 'being gay'
@bot.event
async def on_ready():
    print('bot connected')
    await bot.change_presence(activity=discord.Game("Being Gay"))


# class to send messages upon joining
class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    # listener that looks if someone joined and will reply if someone joined
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            greeting = "Hello, Welcome to the greatest server of all time"
            await channel.send(greeting)


@bot.event
async def on_message(message):
    # don't reply to ourselves
    if message.author.id == bot.user.id:
        return

    # don't reply to other bots
    if message.author.bot:
        return

    # reply to @ mentions
    if bot.get_user(fubyID) in message.mentions:
        response = "Hi, I'm Fuby and I'm cute!"
        await message.channel.send(response, delete_after=60)

    # reply to other various messages
    if "iron forge" in message.content:
        response = "that's a trash upgrade"
        await message.channel.send(response)

    await bot.process_commands(message)


# command checks if bot is up
@bot.command(name='test', help='test if the bot is working')
async def test(ctx):
    response = 'Don\'t worry, I\'m working!'
    await ctx.send(response)


# command chooses a random compliment out of the list of compliments in data.py
@bot.command(name='compliment', help='admire fuby randomly')
async def compliment(ctx):
    response = random.choice(compliments)
    await ctx.send(response)


# get the FubyCutieFan server invite
@bot.command(name='invite', help='get the server invite')
async def invite(ctx):
    response = "https://discord.gg/2UQq8vG"
    await ctx.send(response)


# get the hammerSMP invite
@bot.command(name='server', help='get the name and link of fubys main minecraft server')
async def compliment(ctx):
    response = f'HammerSMP best server uwu\n' \
               f'https://discord.gg/QMuwbqa'
    await ctx.send(response)


bot.add_cog(Greetings(bot))
bot.run(TOKEN)
