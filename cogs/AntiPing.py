import discord
from discord.ext import commands
import logging
log = logging.getLogger("integza.cogs.AntiPinger")

ping_blacklist = [
    414918675481493506
]

intpingembed = discord.Embed(
    title="Dont ping integza please!", description="Please read rule 10, if you ping integza there is a lower chance he will see it!", color=0x0c0f27)


class AntiPinger(commands.Cog, name = "Anti Integza Pinger"):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        #Dont respond to bots
        if message.author.bot:
            return
        
        for mention in message.mentions:
            if mention.id in ping_blacklist:
                await message.channel.send("||<@275291687637745665> <@" + str(message.author.id) +">||", embed = intpingembed)
                log.info("User %s (Id: %s) pinged %s" % (str(message.author), message.author.id, mention.id))
                break
            
