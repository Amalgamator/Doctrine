import discord
from discord.ext import commands


class Admin(commands.Cog):
    """Administrative commands, listeners, and optional states."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # Listens for msgs with command prefix
    @commands.has_role(786679773866098708)  # message author has dev role
    @commands.guild_only()  # No private messages
    async def hello(self, ctx):
        """Responds with a hello message if a dev says hello."""
        await ctx.send('Hello developer {0.display_name}.'.format(ctx.author))


def setup(bot):
    bot.add_cog(Admin(bot))
