import discord
import random
from discord.ext import commands
from pymongo import MongoClient

# no requests, because default is aiohttp

dbclient = MongoClient('localhost', 27017)
db = dbclient.doctrine


def generate_mappool():
    mappool = {}
    for doc in db.mappool.find():
        map = {}
        for k, v in doc.items():
            if k == "_id":
                pass
            else:
                map[k] = v
        mappool.append(map)
    return mappool


class Pools(commands.Cog):
    """Commands pertaining to map and civ pools."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="randmap", aliases=["pickmap", "getmap"])  # Listens for msg with prefix
    @commands.guild_only()  # No private messages
    async def randmap(self, ctx, *, message: str):
        """Responds with a single map, based on label constraints."""
        labels = message.lower().split(' ')
        filters = {}
        for label in labels:
            if label[0] == "-":
                label = label[1:]
                filters[label] = 0
            else:
                filters[label] = 1
        maps = []
        for doc in db.mappool.find(filters):
            maps.append(doc["name"])
        selection = random.choice(maps)
        await ctx.send(selection)

    @commands.command()  # Listens for msgs with command prefix
    @commands.guild_only()  # No private messages
    async def listmaps(self, ctx, *, message: str):
        """Responds with a list of maps, based on label constraints."""
        labels = message.lower().split(' ')
        filters = {}
        print(filters)
        for label in labels:
            if label[0] == "-":
                label = label[1:]
                filters[label] = 0
            else:
                filters[label] = 1
        maps = []
        for doc in db.mappool.find(filters):
            maps.append(doc["name"])
        print(maps)
        response = "```"
        for item in maps:
            response = response + "\n" + item
        print(response)
        response = response + "```"
        await ctx.send(response)


def setup(bot):
    bot.add_cog(Pools(bot))
