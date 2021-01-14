import logging
import discord
from systemd.journal import JournalHandler
from discord.ext import commands

# Set up logging for doctrine bot through systemd journaller
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = JournalHandler()
logformat = '%(asctime)s:%(levelname)s:%(name)s: %(message)s'
handler.setFormatter(logging.Formatter(logformat))
logger.addHandler(handler)


class Boar(commands.Cog):
    """Commands involving the Build Order AlgoRithm."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # Listens for msgs with command prefix
    @commands.guild_only()  # No private messages
    async def boar(self, ctx):
        """Placeholder boar command."""
        await ctx.send("I'm boaring {0.display_name}.".format(ctx.author))

def setup(bot):
    bot.add_cog(Boar(bot))
