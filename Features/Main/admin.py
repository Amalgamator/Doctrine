import logging
import discord
import sys
from systemd.journal import JournalHandler
from discord.ext import commands

# Set up logging for doctrine bot through systemd journaller
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = JournalHandler()
logformat = '%(asctime)s:%(levelname)s:%(name)s: %(message)s'
handler.setFormatter(logging.Formatter(logformat))
logger.addHandler(handler)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

class Admin(commands.Cog):
    """Administrative commands, listeners, and optional states."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # Listens for msgs with command prefix
    @commands.has_role(797016628629340200)  # message author has dev role
    @commands.guild_only()  # No private messages
    async def hello(self, ctx):
        """Responds with a hello message if a dev says hello."""
        await ctx.send("Hello developer {0.display_name}.".format(ctx.author))

    @commands.command()  # Listens for msgs with command prefix
    @commands.has_role(797016628629340200)  # message author has dev role
    @commands.guild_only()  # No private messages
    async def reload(self, ctx):
        """Reloads all extensions."""
        try:
            for extension in self.bot.extensions:
                self.bot.reload_extension(extension)
            await ctx.send("{0.display_name} Reloaded cogs.".format(ctx.author))
        except Exception as e:
            await ctx.send("{0.display_name} Failed. Rolling back.".format(ctx.author))
            logger.debug("Reloading extension '%s' failed: %s",
                         extension,
                         e)


    @commands.command(aliases=["reboot"])  # Listens for msgs with command prefix
    @commands.has_role(797016628629340200)  # message author has dev role
    @commands.guild_only()  # No private messages
    async def restart(self, ctx):
        """Restarts the bot itself."""
        logger.debug("Received restart command from %s", ctx.author)
        await ctx.message.delete()
        message = await ctx.send("Restarting. Please allow 30s to pass...")
        restart_program()


def setup(bot):
    bot.add_cog(Admin(bot))
