import discord
import random
from discord.ext import commands


class Challenge(commands.Cog):
    """Commands and events related to the challenge channel."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="challenge")
    @bot.command()
    async def text(self, ctx):
        msg = await ctx.channel.send(' the text ')
        await msg.add_reaction('🏆')
    @client.event
    async def on_reaction_add(reaction, user):
        if reaction.emoji('🏆'):
            await reaction.channel.send('Test')

def setup(bot):
    bot.add_cog(Challenge(bot))
