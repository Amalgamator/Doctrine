import os
import logging
import requests
import discord

from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime

# Set up logging for doctrine bot client
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

# Define scope (intents) of the client.
intents = discord.Intents.default()
intents.members = True
intents.typing = False
intents.presences = False
intents.messages = True
intents.reactions = True

client = commands.Bot(command_prefix="d!", help_command=None, intents=intents)

cogs = ["Features.Main.admin"  # admin, handler, log routines
        # "Features.Engine",  # game info commands
        # "Features.Elo",  # player info commands
        # "Features.Boar",  # Build Order AlgoRithm
        # "Features.Misc",  # additional cogs
        ]


@client.event
async def on_ready():
    with open('main.log', 'a') as f:
        now = datetime.now()
        dt_str = now.strftime("%Y/%m/%d %H:%M:%S")
        logstr = "\n"+dt_str+': Succes! Logged in as {0.user}'.format(client)
        f.write(logstr)
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game(os.getenv('BotStatus')))
    for cog in cogs:
        try:
            print(f"Loading cog {cog}...")
            client.load_extension(cog)
            print(f"Loaded cog {cog}!")
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print("Failed to load cog {}\n{}".format(cog, exc))

client.run(TOKEN)
