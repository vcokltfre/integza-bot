from discord.ext import commands
from discord import Intents, AllowedMentions, Game

from loguru import logger
from traceback import format_exc

from src.utils.database import Database


class Bot(commands.Bot):
    """A subclass of commands.Bot with additional functionality."""

    def __init__(self, *args, **kwargs):
        logger.info("Starting up...")

        intents = Intents.all()

        super().__init__(
            command_prefix=">",
            intents=intents,
            allowed_mentions=AllowedMentions(roles=False, everyone=False),
            activity=Game(name="Annihilating Tomatos!"),
            *args,
            **kwargs
        )

        self.db: Database = Database()

    def load_extensions(self, *exts) -> None:
        """Load a given set of extensions."""

        logger.info(f"Starting loading {len(exts)} extensions...")

        success = 0

        for ext in exts:
            try:
                self.load_extension(ext)
            except Exception as e:
                logger.error(f"Error while loading {ext}: {e}:\n{format_exc()}")
            else:
                logger.info(f"Successfully loaded extension {ext}.")
                success += 1

        logger.info(f"Extension loading finished. Success: {success}. Failed: {len(exts) - success}.")

    async def login(self, *args, **kwargs) -> None:
        """Create the database connection before login."""
        logger.info("Logging in to Discord...")

        await self.db.setup()

        await super().login(*args, **kwargs)

    async def on_connect(self):
        """Log the connect event."""

        logger.info("Connected to Discord.")
