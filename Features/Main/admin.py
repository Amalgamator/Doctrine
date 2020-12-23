import discord
from discord.ext import commands


class admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role(786679773866098708)
    @commands.guild_only()
    async def hello(self, ctx):
        await ctx.send('Hello developer {0.display_name}.'.format(ctx.author))


def setup(bot):
    bot.add_cog(admin(bot))
