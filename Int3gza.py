import discord
import random
import asyncio
import logging
from discord.ext import commands

#  VARIABLES  #
my_last_message = ""
dadude = ""
bot = commands.Bot(command_prefix = '>')
TOKEN = "Nzc0MzEzMjg3NDQ1NTEyMjcy.X6V9cQ.pRNWDbBie59EDtwXOZE6eboobmY"
printsend = 0
metalsend = 0

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
    global printsend
    global metalsend
    if ("3d print metal" in message.content):
        if metalsend == 0:
            my_last_message = await message.channel.send(embed=metalembed, delete_after= 10)
            #await my_last_message.add_reaction("🗑️")
            metalsend = 1
    if ("print metal" in message.content):
        if metalsend == 0:
            my_last_message = await message.channel.send(embed=metalembed, delete_after= 10)
            #await my_last_message.add_reaction("🗑️")
            metalsend = 1
    if ("metal printer" in message.content):
        if metalsend == 0:
            my_last_message = await message.channel.send(embed=metalembed, delete_after= 10)
            #await my_last_message.add_reaction("🗑️")
            metalsend = 1
    if ("printer should" in message.content):
        if printsend == 0:
            my_last_message = await message.channel.send(embed=printembed, delete_after= 120)
            #await my_last_message.add_reaction("🗑️")
            printsend = 1
    if ("good printer" in message.content):
        if printsend == 0:
            my_last_message = await message.channel.send(embed=printembed, delete_after= 120)
            #await my_last_message.add_reaction("🗑️")
            printsend = 1
    if ("i buy" in message.content):
        if printsend == 0:
            my_last_message = await message.channel.send(embed=printembed, delete_after= 120)
            #await my_last_message.add_reaction("🗑️")
            printsend = 1
    if ("what printer" in message.content):
        if printsend == 0:
            my_last_message = await message.channel.send(embed=printembed, delete_after= 120)
            #await my_last_message.add_reaction("🗑️")
            printsend = 1
    if ("i should buy" in message.content):
        if printsend == 0:
            my_last_message = await message.channel.send(embed=printembed, delete_after= 120)
            #await my_last_message.add_reaction("🗑️")
            printsend = 1
    
    printsend = 0
    metalsend = 0

    if("@" in message.content):
        if(message.mentions[0].id == 414918675481493506):
            await message.channel.send("||<@275291687637745665> <@" + str(message.author.id) +">||", embed = intpingembed)
    if(message.content == ">ping"):
        pingembed = discord.Embed(title="Ping", color=0x0c0f27)
        pingembed.add_field(name="Bot", value=f'🏓 Pong! {round(bot.latency * 1000)}ms')
        pingembed.set_footer(text=f"Request by {message.author}", icon_url=message.author.avatar_url)
        await message.channel.send(embed=pingembed)

        
@bot.event
async def on_reaction_add(message, reaction, user):
    global my_last_message
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
