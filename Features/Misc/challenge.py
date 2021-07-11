import discord
import random
from discord.ext import commands


class Challenge(commands.Cog):
    """Commands and events related to the challenge channel."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="challenge")
    async def something():
    #
    """
    0) challenger mentions @challengee with keyword challenge
    1) mentioned user becomes role 'challengee'
    2) enable listener: "if challenger reacts with trophy,
        challengee becomes role challenger,
        remove challenger role from challenger"
    3) if challenger challenges previous challenger, ignore
    4)
    """

def setup(bot):
    bot.add_cog(Challenge(bot))
