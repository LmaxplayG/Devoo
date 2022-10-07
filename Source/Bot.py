import datetime
from os import getcwd
import os
from random import random
import sys
import discord
from discord.ext import commands
import random
import secrets
import copy

from Modules.Commands import Register as RegisterCommands
from Modules.Config import Config
from Modules.Events import Register as RegisterEvents
from Modules.Commands.About import About

import dotenv
import pathlib

#import stripe


# CONFIG


intents = discord.Intents.all()

bot = commands.AutoShardedBot(intents=intents, description="Test", command_prefix=random.random().__str__())

# Register cogs
RegisterCommands(bot)
RegisterEvents(bot)

if Config.RELEASE == 'Release':
    bot.run(dotenv.get_key(pathlib.Path(__file__).parent.joinpath("./.env"), "TOKEN"))
else:
    bot.run(dotenv.get_key(pathlib.Path(__file__).parent.joinpath("./.env"), "TOKEN_DEV"))
