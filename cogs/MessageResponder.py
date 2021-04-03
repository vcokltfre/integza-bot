import discord
from discord.ext import commands
import logging
import re
log = logging.getLogger("integza.cogs.MessageResponder")
trigger_log = logging.getLogger("integza.cogs.MessageResponder.trigger")

class MessageResponce:
    def __init__(self, name, filters, responce, delete_after = 120):
        if (type(filters) != list):
            filters = [filters]

        #Normalize all string filters to regex
        for index, value in enumerate(filters):
            if (type(value) == str):
                filters[index] = re.compile(re.escape(value), re.IGNORECASE)

        self.name = name
        self.filters = filters
        self.response = responce
        self.delete_after = delete_after

    async def respond(self, channel):
        if (type(self.response) == discord.Embed):
            await channel.send(embed = self.response, delete_after = self.delete_after)
        else:
            await channel.send(self.response, delete_after = self.delete_after)

    def shouldRespond(self, messageText):
        return any(filter.search(messageText) != None for filter in self.filters)
    
responses = [
    MessageResponce("PrinterBuy", ["printer should","good printer","i buy","what printer","i should buy","buy a 3d printer"],
                    discord.Embed(title="What printer should I get?", description="", color=0x0c0f27)
                        .add_field(name="Prusa MK3S", value="The Prusa is a great printer overall, it is quite expensive but worth it. Great option if you arent on a budget and works amazing out of the box  \n **Price: U$D 750** \n \n", inline=False)
                        .add_field(name="Creality Ender 3", value="The ender 3 is a great printer overall, a great Prusa clone. It is a mid range printer that can get up to Prusa performance with some tweaking \n **Price: U$D 200** \n \n", inline=False)
                        .add_field(name="FLSUN QQ-S Pro", value="The QQ-S is a great delta printer at an amazing price, the big brother of the Q5 \n **Price: U$D 364** \n \n", inline=False)
                        .add_field(name="Elegoo Mars", value="The mars is a great sla printer for a good price, resin printers take time to use, so if you are looking for a prototyping machine that can output models fast get an FDM printer \n **Price: U$D 190** \n \n ", inline=False)
                        .add_field(name="Elegoo Mars Pro 2", value="Its a very fast printer, it packs an lcd uv screen that can print at two seconds per layer. It is the printer I use to print Porcelite \n **Price: U$D 350**", inline=False)),
    
    MessageResponce("MetalPrinter", [ "3d print metal","print metal","metal printer"],
                     discord.Embed(title="a metal printer costs more than my entire net worth!", description="Wont happen", color=0x0c0f27)),

    MessageResponce("StarliteVideo", re.compile("0IbWampaEcM"),
                    discord.Embed(title="I already saw that video!", description = "around 169 times to be precise", color=0x0c0f27))
]


class MessageResponder(commands.Cog, name = "Message responder"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "resp")
    async def play_reponse(self, ctx, msg_response: str):
        for response in responses:
            if response.name.lower() == msg_response.lower():
                await response.respond(ctx)
                log.info("User triggered response \"%s\" manually", response.name)
                break
    
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        #Dont respond to bots
        if message.author.bot:
            return

        #Dont respond to dms for message responder cog
        if not message.guild:
            return

        for response in responses:
            if response.shouldRespond(message.content):
                trigger_log.info("User \"%s\" triggered response \"%s\"" % (message.author.name+"#"+message.author.discriminator, response.name))
                await response.respond(message.channel)
                break
        
    
