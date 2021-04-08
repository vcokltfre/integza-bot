from discord import Embed, Message
from discord.ext import commands

from time import time
from collections import namedtuple

from src.internal.bot import Bot
from src.utils.responder import respond


Result = namedtuple("Result", ["result", "time"])


class Core(commands.Cog):
    """A cog of general bot commands."""

    def __init__(self, bot: Bot):
        self.bot = bot

    @staticmethod
    async def timed_coro(coro) -> Result:
        ts = time()
        res = await coro
        return Result(res, round((time() - ts) * 1000, 2))

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        await respond(message)

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """Get the bot's API ping and websocket latency."""

        m_send = await self.timed_coro(ctx.send("Testing ping..."))
        m_edit = await self.timed_coro(m_send.result.edit(content="Edit test."))
        m_delete = await self.timed_coro(m_send.result.delete())

        embed = Embed(
            title="Bot Ping",
            timestamp=ctx.message.created_at,
            colour=0x87CEEB,
        )

        embed.add_field(name="API Send", value=f"{m_send.time}ms")
        embed.add_field(name="API Edit", value=f"{m_edit.time}ms")
        embed.add_field(name="API Delete", value=f"{m_delete.time}ms")
        embed.add_field(name="WS Latency", value=f"{round(self.bot.latency * 1000, 2)}ms")

        await ctx.reply(embed=embed)


def setup(bot: Bot):
    bot.add_cog(Core(bot))
