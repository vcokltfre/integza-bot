import discord
import random
import asyncio
import logging
import os
from discord.ext import commands
import importlib
import os.path
import sys
import inspect

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass


#Setup root logging
rootLogger = logging.getLogger()

#Setup loggin handler
handler = logging.StreamHandler(sys.stdout)
rootLogger.addHandler(handler)


#If in debug mode, set the integza logging to debug, else set it to warnings
if os.getenv("DEBUG") == "1":
    logging.getLogger("integza").setLevel(logging.DEBUG)
else:
    logging.getLogger("integza").setLevel(logging.WARNING)


log = logging.getLogger("integza.core")



COG_DIRECTORY = "cogs"

bot = commands.Bot(command_prefix = '>')



for cog_file in os.listdir(COG_DIRECTORY):
    if cog_file == "__pycache__":
        continue
    
    if (not cog_file.endswith('.py') or not os.path.isfile(os.path.join(COG_DIRECTORY, cog_file))):
        log.debug("Ignoring path/file \"%s\"" % cog_file)
        continue
    
    try:
        cog_module_name = cog_file.replace('.py', '')
        cog_import_name = COG_DIRECTORY + "." + cog_module_name
        #TODO: pass in the current bot object as a global
        cog_module = importlib.import_module(cog_import_name)
        log.debug("Imported cog " + cog_import_name)

        #Enumerate through all the exports of the module, if there is a module
        #that extends commands.cogs add it to the bot
        
        for name, value in cog_module.__dict__.items():
            if (not inspect.isclass(value)):
                #log.debug("Ignoring %s from %s" % (name, cog_import_name))
                continue
            
            if (issubclass(value, commands.Cog)):
                log.info("Registering cog class \"%s\"" % (cog_import_name+'.'+name))
                bot.add_cog(value(bot))
            
    except Exception as e:
        log.critical("Cog module \"%s\" failed to load with exception:\n%s"%(cog_file, str(e)))
    


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Destroying Tomatos!'))
    log.info('Logged in as \"%s\" (Id: %s)' % (bot.user.name, bot.user.id))



@bot.event
async def on_command_error(ctx, error):
    logging.error(f'Error on command {ctx.invoked_with}, {error}')
    


log.info("Bot loaded, running now")
assert os.getenv('DISCORD_TOKEN') != None
bot.run(os.getenv('DISCORD_TOKEN'))
