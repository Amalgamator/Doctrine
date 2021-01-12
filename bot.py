import os
import logging
import discord

from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime

from systemd.journal import JournalHandler

# Set up logging for doctrine bot through systemd journaller
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = JournalHandler()
logformat = '%(asctime)s:%(levelname)s:%(name)s: %(message)s'
handler.setFormatter(logging.Formatter(logformat))
logger.addHandler(handler)

# permissions bit int
# 649280

# Get token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
prefix = os.getenv('BOT_PREFIX')
# Define scope (intents) of the bot.
intents = discord.Intents.default()
intents.members = True
intents.typing = False
intents.presences = False
intents.messages = True
intents.reactions = True

bot = commands.Bot(command_prefix=prefix, help_command=None, intents=intents)

cogs = ["Features.Main.admin",  # admin, handler, log routines
        #"Features.Main.info",  # help, bot info, server info
        "Features.Main.error_handler",  # ll
        # "Features.Engine",# game info comnds
        "Features.Elo.basic",  # player info commands
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


@bot.event
async def on_command_completion(ctx):
	fullCommandName = ctx.command.qualified_name
	split = fullCommandName.split(" ")
	executedCommand = str(split[0])
	print(f"Executed {executedCommand} command in {ctx.guild.name} by {ctx.message.author} (ID: {ctx.message.author.id})")


@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		embed = discord.Embed(
			title="Error!",
			description="This command is on a %.2fs cooldown" % error.retry_after,
			color=discord.Colour.from_rgb(255,109,36)
		)
		await ctx.send(embed=embed)
	raise error


@bot.event
async def on_voice_state_update(member, prev, cur):
    """Sets the bot status to watching whichever stream has priority, if any."""
    if prev.channel and cur.channel:  # member is connected before and after
        if prev.self_stream != cur.self_stream:
            # cur.self_stream = True if member is currently streaming
            if cur.self_stream:
                activitystr = f" {member.display_name} | {prefix}"
                await bot.change_presence(
                    activity=discord.Activity(
                        type=discord.ActivityType.watching, name=activitystr))
                print(f"Watching stream of {member}")


# Run the bot with the TOKEN
bot.run(TOKEN, bot=True, reconnect=True)
