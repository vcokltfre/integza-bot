import discord
import random
import asyncio
import logging
import os
from discord.ext import commands

#  VARIABLES  #
my_last_message = ""
dadude = ""
bot = commands.Bot(command_prefix = '>')
TOKEN = os.getenv('DISCORD_TOKEN')

printsend = 0
metalsend = 0


# TRIGGERS #

metalTriggers = [ "3d print metal","print metal","metal printer"]
printTriggers = [ "printer should","good printer","i buy","what printer","i should buy","buy a 3d printer"]

#  Embeds  #

#  Metal  printer Embed  #
metalembed = discord.Embed(
        title="a metal printer costs more than my entire net worth!", description="Wont happen", color=0x0c0f27)

# printers embed #
printembed = discord.Embed(
    title="What printer should I get?", description="", color=0x0c0f27)
printembed.add_field(
    name="Prusa MK3S", value="The Prusa is a great printer overall, it is quite expensive but worth it. Great option if you arent on a budget and works amazing out of the box  \n **Price: U$D 750** \n \n", inline=False)
printembed.add_field(
    name="Creality Ender 3", value="The ender 3 is a great printer overall, a great Prusa clone. It is a mid range printer that can get up to Prusa performance with some tweaking \n **Price: U$D 200** \n \n", inline=False)
printembed.add_field(
    name="FLSUN QQ-S Pro", value="The QQ-S is a great delta printer at an amazing price, the big brother of the Q5 \n **Price: U$D 364** \n \n", inline=False)
printembed.add_field(
    name="Elegoo Mars", value="The mars is a great sla printer for a good price, resin printers take time to use, so if you are looking for a prototyping machine that can output models fast get an FDM printer \n **Price: U$D 190** \n \n ", inline=False)
printembed.add_field(
    name="Elegoo Mars Pro 2", value="Its a very fast printer, it packs an lcd uv screen that can print at two seconds per layer. It is the printer I use to print Porcelite \n **Price: U$D 350**", inline=False)

# Integza Ping Embed #

intpingembed = discord.Embed(
    title="Dont ping integza please!", description="Please read rule 10, if you ping integza there is a lower chance he will see it!", color=0x0c0f27)

# Starlite embed #

starliteembed = discord.Embed(
    title="I already saw that video!", description = "around 169 times to be precise", color=0x0c0f27)

# Mod help embed

modhelp = discord.Embed(
    title="Mod help", description="", color=0x0c0f27)
modhelp.add_field(
    name="When to warn", value="If someone breaks a rule you should warn them and state the reason, if they complain explain to them your reasoning. if you are unsure if you should warn dont hesitate to ping marco or other staff in mod chat", inline=False)
modhelp.add_field(
    name="When to kick", value="If someone keeps breaking the rules warn them every time they do so mee6 can deal with teh amount of times a person can break rules and administer the proper punishment", inline=False)
modhelp.add_field(
    name="Someone is asking me for mod!", value="When someone asks to be a moderator or a staff memeber tell them to open a ticket so staff can accept or deny their request", inline=False)
modhelp.add_field(
    name="Someone is mini modding!", value="when someone is Mini modding tell them to stop and let them know that its not okay, mini modding isnt warnable, give them a verbal warning", inline=False)
modhelp.add_field(
    name="The server is being raided what do i do!", value="Ping every staff thats above you, raided means at least 5 people are executing a coordinated attack, such as spam or flooding", inline=False)


#  Start  #

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Destroying Tomatos!'))
    print("--------------------")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------')
    return

#  On Message  #

@bot.event
async def on_message(message):
    global my_last_message
    global printembed
    global intpingembed
    global metalembed
    
    if any(trg in message.content for trg in metalTriggers):
        my_last_message = await message.channel.send(embed=metalembed, delete_after= 120)
        #await my_last_message.add_reaction("🗑️")
    
    if any(trg in message.content for trg in printTriggers):
        my_last_message = await message.channel.send(embed=printembed, delete_after= 120)
        #await my_last_message.add_reaction("🗑️")

    if("0IbWampaEcM" in message.content):
        await message.channel.send("||<@" + str(message.author.id) +">||", embed = starliteembed)
        
    if(message.author == 414918675481493506):
        chance = random.randint(1,10)
        if(chance > 7):
            message.channel.send("Shut up integza!")
    
    if("@" in message.content):
        for mention in message.mentions:
            if(mention.id == 414918675481493506):
                await message.channel.send("||<@275291687637745665> <@" + str(message.author.id) +">||", embed = intpingembed)
            
    if(message.content == ">ping"):
        pingembed = discord.Embed(title="Ping", color=0x0c0f27) 
        pingembed.add_field(name="Bot", value=f'🏓 Pong! {round(bot.latency * 1000)}ms')
        pingembed.set_footer(text=f"Request by {message.author}", icon_url=message.author.avatar_url)
        await message.channel.send(embed=pingembed)

    if(message.content == ">modhelp"):
        for role in message.author.roles:
            if role.name == "Helper":
                await bot.get_user(message.author).send(embed = modhelp)

        
@bot.event
async def on_reaction_add(message, reaction, user):
    global my_last_message
    if message.author == bot.user:
        if user != bot.user:
            if str(reaction.emoji) == "🗑️":
                await my_last_message.delete(my_last_message)

@bot.event
async def on_command_error(ctx, error):
    logging.error(f'Error on command {ctx.invoked_with}, {error}')
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="Error!",
                              description=f"The command `{ctx.invoked_with}` was not found! We suggest you do `.help` to see all of the commands",
                              colour=0xe73c24)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRole):
        embed = discord.Embed(title="Error!",
                              description=f"You don't have permission to execute `{ctx.invoked_with}`.",
                              colour=0xe73c24)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error!",
                              description=f"`{error}`",
                              colour=0xe73c24)
        await ctx.send(embed=embed)
        raise error

bot.run(TOKEN)
