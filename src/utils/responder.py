from discord import Embed, Message
from re import compile


metalTriggers = [compile(x) for x in ["3d print metal", "print metal", "metal printer"]]

printTriggers = [
    compile(x)
    for x in [
        "printer should",
        "good (3d|resin) printer",
        "what printer",
        "i should buy",
        "buy a 3d printer",
    ]
]

starliteTriggers = [compile(x) for x in ["0IbWampaEcM"]]

metalembed = Embed(
    title="a metal printer costs more than my entire net worth!",
    description="Wont happen",
    color=0x0C0F27,
)

# printers embed #
printembed = Embed(title="What printer should I get?", description="", color=0x0C0F27)
printembed.add_field(
    name="Prusa MK3S",
    value="The Prusa is a great printer overall, it is quite expensive but worth it. Great option if you arent on a budget and works amazing out of the box  \n **Price: U$D 750** \n \n",
    inline=False,
)
printembed.add_field(
    name="Creality Ender 3",
    value="The ender 3 is a great printer overall, a great Prusa clone. It is a mid range printer that can get up to Prusa performance with some tweaking \n **Price: U$D 200** \n \n",
    inline=False,
)
printembed.add_field(
    name="FLSUN QQ-S Pro",
    value="The QQ-S is a great delta printer at an amazing price, the big brother of the Q5 \n **Price: U$D 364** \n \n",
    inline=False,
)
printembed.add_field(
    name="Elegoo Mars",
    value="The mars is a great sla printer for a good price, resin printers take time to use, so if you are looking for a prototyping machine that can output models fast get an FDM printer \n **Price: U$D 190** \n \n ",
    inline=False,
)
printembed.add_field(
    name="Elegoo Mars Pro 2",
    value="Its a very fast printer, it packs an lcd uv screen that can print at two seconds per layer. It is the printer I use to print Porcelite \n **Price: U$D 350**",
    inline=False,
)

starliteembed = Embed(
    title="I already saw that video!",
    description="around 169 times to be precise",
    color=0x0C0F27,
)

intpingembed = Embed(
    title="Dont ping integza please!",
    description="Please read rule 10, if you ping integza there is a lower chance he will see it!",
    color=0x0C0F27,
)

async def respond(message: Message):
    for trigger in metalTriggers:
        if trigger.match(message.content):
            return await message.reply(embed=metalembed)
    for trigger in printTriggers:
        if trigger.match(message.content):
            return await message.reply(embed=printembed)
    for trigger in starliteTriggers:
        if trigger.match(message.content):
            return await message.reply(embed=starliteembed)
    for mention in message.mentions:
        if mention.id == 414918675481493506:
            return await message.reply(embed=intpingembed)
