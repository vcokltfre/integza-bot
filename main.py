from os import getenv
from dotenv import load_dotenv

from src.internal.bot import Bot


load_dotenv()

bot = Bot()

bot.load_extensions(
    #"jishaku",
    "src.cogs.core",
)

bot.run(getenv("DISCORD_TOKEN"))