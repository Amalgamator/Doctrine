import discord
import random
from discord.ext import commands
from pymongo import MongoClient

dbclient = MongoClient('localhost', 27017)
db = dbclient.doctrine
coll = db.units

class Ludus(commands.Cog):
    """Commands pertaining to objects and their combat abilities."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="duel", aliases=["fight", "vs"])  # Listens for msg with prefix
    @commands.guild_only()  # No private messages
    async def duel(self, ctx, *args: str):
        """Responds with a single map, based on arg constraints."""
        filters = {}
        for arg in args:
            pass
            # find the arg in db docs

        # Embed with icons & unit attributes

            await ctx.send("Let's go!")

def setup(bot):
    bot.add_cog(Pools(bot))
