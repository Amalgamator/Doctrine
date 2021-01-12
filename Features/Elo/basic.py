import discord
import random
from discord.ext import commands


class BasicELO(commands.Cog):
    """Commands pertaining to objects and their combat abilities."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="duel", aliases=["fight", "vs"])  # Listens for msg with prefix
    @commands.guild_only()  # No private messages
    async def live(self, ctx, *args: str):

        response = "you're a noob"
        await ctx.send(response)

def setup(bot):
    bot.add_cog(BasicELO(bot))
