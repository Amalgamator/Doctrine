import discord
import random
from discord.ext import commands
from pymongo import MongoClient

dbclient = MongoClient('localhost', 27017)
db = dbclient.doctrine
coll = db.units

class Ludus(commands.Cog):
    """Commands pertaining to objects info from the engine files, like units."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="duel", aliases=["fight", "vs"])  # Listens for msg with prefix
    @commands.guild_only()  # No private messages
    async def duel(self, ctx, *args: str):
        """Responds with the result of a duel."""
        await ctx.send(f"Let's go!")

def setup(bot):
    bot.add_cog(Ludus(bot))
