from discord import Embed
from discord.ext import commands

from src.internal.bot import Bot


class Core(commands.Cog):
    """A cog of general bot commands."""

    def __init__(self, bot: Bot):
        self.bot = bot




def setup(bot: Bot):
    bot.add_cog(Core(bot))