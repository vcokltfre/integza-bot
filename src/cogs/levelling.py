from discord import Embed, Message
from discord.ext import commands
from aiohttp import ClientSession
from json import loads

from datetime import timedelta
from random import randint

from src.internal.bot import Bot


class Levelling(commands.Cog):
    """XP and levelling."""

    def __init__(self, bot: Bot):
        self.bot = bot

    @staticmethod
    def calculate_user_xp_data(user_xp: int):
        base_xp = 360
        total_xp = 0
        lvl = 1

        while True:
            required_xp_to_level_up = int(base_xp + base_xp / 4.0 * (lvl - 1))

            if required_xp_to_level_up + total_xp > user_xp:
                break

            total_xp += required_xp_to_level_up
            lvl += 1

        return lvl, user_xp - total_xp, required_xp_to_level_up

    async def get_now(self):
        return (await self.bot.db.fetchrow("SELECT NOW();"))["now"]

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        user = await self.bot.db.get_user(message.author.id)

        if user["last_xp"] + timedelta(seconds=30) < await self.get_now():
            await self.bot.db.update_user_xp(message.author.id, randint(20, 40))

    @commands.command(name="rank", aliases=["level", "xp"])
    async def get_xp(self, ctx: commands.Context):
        embed = Embed(
            title=f"XP | {ctx.author}",
            colour=0x87CEEB,
            timestamp=ctx.message.created_at,
            description="",
        )

        user = await self.bot.db.get_user(ctx.author.id)
        rank_data = self.calculate_user_xp_data(user["xp"])

        embed.description += f"XP: {user['xp']}\n"
        embed.description += f"Level: {rank_data[0]}\n"
        embed.description += f"Level up in {rank_data[2]}xp"

        await ctx.reply(embed=embed)

    @commands.command(name="importmee6")
    async def importmee6(self, ctx: commands.Context):
        if ctx.author.id != 297045071457681409:
            return

        sess = ClientSession()

        at = ctx.message.attachments[0].url

        data = await (await sess.get(at)).text()

        data = loads(data)

        for user in data:
            xp = user["xp"]
            id = int(user["id"])

            await self.bot.db.update_user_xp(id, xp)

        return await ctx.reply(f"Successfully imported XP from {len(data)} MEE6 users.")


def setup(bot: Bot):
    bot.add_cog(Levelling(bot))
