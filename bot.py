import os
import logging
import discord
import glob
from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime
from os.path import isfile, join

from systemd.journal import JournalHandler

# Set up logging for bot through systemd journaller
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


# Load the cog directory
cog_dir = str(os.path.dirname(os.path.realpath(__file__))+"/Features")

def get_cogs(cog_dir):
    file_list = []
    for dir_, _, files in os.walk(cog_dir):
        for file_name in files:
            if file_name.endswith(".py"):
                rel_dir = os.path.relpath(dir_, cog_dir)
                rel_file = os.path.join(rel_dir, file_name).replace("\\",".").replace("/",".").strip(".py")
                rel_file = "Features."+rel_file
                file_list.append(rel_file)
    print(file_list)
    return file_list

# Set the list of cogs to load
try:
    cogs = get_cogs(cog_dir)
    logger.debug("Files loaded %s ", cogs)
except:
    logger.debug("Files failed to load.")
    os._exit(1)

if __name__ == '__main__':
    for cog in cogs:
        try:
            logger.debug("Loading cog %s...", cog)
            bot.load_extension(cog)
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            logger.debug("Loading cog %s failed with Error: %s", cog, e)


@bot.event
async def on_ready():
    na = str(bot.user.name)
    id = str(bot.user.id)
    ve = str(discord.__version__)
    logger.debug('\nLogged in as: %s - %s\nVersion: %s\n', na, id, ve)
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game(os.getenv('BotStatus')))


@bot.event
async def on_command_completion(ctx):
    fullCName = ctx.command.qualified_name
    co = str(fullCName.split(" ")[0])
    logger.debug("Executed %s comm. in %s by %s (ID: %s)",
                 co,
                 ctx.guild.name,
                 ctx.message.author,
                 ctx.message.author.id)


@bot.event
async def on_command_error(ctx, error):
    fullCName = ctx.command.qualified_name
    co = str(fullCName.split(" ")[0])
    error = getattr(error, 'original', error)
    logger.debug("FAILED COMM.%s IN %s BY %s (ID: %s) \n %s",
                 co,
                 ctx.guild.name,
                 ctx.message.author,
                 ctx.message.author.id,
                 error)

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
                logger.debug("Watching stream of %s",
                             member)


# Run the bot with the TOKEN
try:
    bot.run(TOKEN, bot=True, reconnect=True)
except Exception as e:
    logger.debug("Bot run failed: ",
                 e)
