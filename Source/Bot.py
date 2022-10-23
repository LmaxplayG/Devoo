from random import random
import discord
from discord.ext import commands
import random

from Modules.Commands import Register as RegisterCommands
from Modules.Config import Config
from Modules.Events import Register as RegisterEvents

import dotenv
import pathlib


intents = discord.Intents.all()

bot = commands.AutoShardedBot(intents=intents, description="Test", command_prefix=random.random().__str__())

bot.remove_command("help")

RegisterCommands(bot)
RegisterEvents(bot)

if Config.VERSION == 'Release':
    bot.run(dotenv.get_key(pathlib.Path(__file__).parent.joinpath("./.env"), "TOKEN"))
else:
    bot.run(dotenv.get_key(pathlib.Path(__file__).parent.joinpath("./.env"), "TOKEN_DEV"))
