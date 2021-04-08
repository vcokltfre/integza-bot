from os import getenv

from src.internal.bot import Bot


bot = Bot()

bot.load_extensions(
    #"jishaku",
    "src.cogs.core",
    "src.cogs.errors",
    "src.cogs.levelling",
)

bot.run(getenv("DISCORD_TOKEN"))