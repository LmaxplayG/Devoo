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

from Source.Commands import Register as RegisterCommands
from Source.Config import *
from Source.Events import Register as RegisterEvents
from Source.Commands.About import About

import dotenv
import pathlib

#import stripe


# CONFIG


intents = discord.Intents.all()

bot = commands.AutoShardedBot(intents=intents, description="Test", command_prefix=random.random().__str__())

# Register cogs
RegisterCommands(bot)
RegisterEvents(bot)

if RELEASE == 'Release':
    bot.run(dotenv.get_key(pathlib.Path(__file__).parent.joinpath("./.env"), "TOKEN"))
else:
    bot.run(dotenv.get_key(pathlib.Path(__file__).parent.joinpath("./.env"), "TOKEN_DEV"))
