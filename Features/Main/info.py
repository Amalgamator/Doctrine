import discord
from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def help(self, ctx):
        info_board = discord.Embed(
            title="Doctrine",
            description="An Age of Empires II: DE community Discord bot.",
            colour=discord.Colour.from_rgb(109, 255, 234)
        )
        info_board.set_footer(text="Note: Some commands rely on third party services. Don't spam.")
        info_board.add_field(name="```d!help```",
                             value="> Lists and describes commands.",
                             inline=False)
        info_board.add_field(name="```d!hello```",
                             value="> Placeholder test command for devs.",
                             inline=False)
        await ctx.send(content=None, embed=info_board)


def setup(bot):
    bot.add_cog(Info(bot))
