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



class Admin(commands.Cog):
    """Administrative commands, listeners, and optional states."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # Listens for msgs with command prefix
    @commands.has_role(797016628629340200)  # message author has dev role
    @commands.guild_only()  # No private messages
    async def hello(self, ctx):
        """Responds with a hello message if a dev says hello."""
        await ctx.send('Hello developer {0.display_name}.'.format(ctx.author))

    @commands.command()  # Listens for msgs with command prefix
    @commands.has_role(797016628629340200)  # message author has dev role
    @commands.guild_only()  # No private messages
    async def reload(self, ctx):
        """Reloads all extensions."""
        for extension in bot.extensions:
            try:
                bot.reload_extension(extension)
            except Exception as e:
                logger.info(f"Reloading extension '{extension}' failed: "e)

        await ctx.send('{0.display_name} Reloaded cogs.'.format(ctx.author))


def setup(bot):
    bot.add_cog(Admin(bot))
