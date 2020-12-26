import os
import logging
import discord

from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime

# Set up logging for doctrine bot
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='main.log',
                              encoding='utf-8',
                              mode='w')
logformat = '%(asctime)s:%(levelname)s:%(name)s: %(message)s'
handler.setFormatter(logging.Formatter(logformat))
logger.addHandler(handler)


# permissions bit int
# 649280

# Get token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Define scope (intents) of the bot.
intents = discord.Intents.default()
intents.members = True
intents.typing = False
intents.presences = False
intents.messages = True
intents.reactions = True

bot = commands.Bot(command_prefix="d!", help_command=None, intents=intents)

cogs = ["Features.Main.admin",  # admin, handler, log routines
        "Features.Main.info",  # help, bot info, server info
        "Features.Main.error_handler",  # ll
        # "Features.Engine",# game info comnds
        # "Features.Elo",  # player info commands
        # "Features.Boar",  # Build Order AlgoRithm
        "Features.Misc.pools"  # additional commands
        ]

if __name__ == '__main__':
    for cog in cogs:
        try:
            print(f"Loading cog {cog}...")
            bot.load_extension(cog)
            print(f"Loaded cog {cog}!")
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print("Failed to load cog {}\n{}".format(cog, exc))


@bot.event
async def on_ready():
    print(f'\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game(os.getenv('BotStatus')))


bot.run(TOKEN, bot=True, reconnect=True)
