import discord              as Discord
import discord.ext.commands as Commands
import random               as Random
import dotenv               as DotEnv
import pathlib              as Pathlib

from Modules.Commands import Register as RegisterCommands
from Modules.Events   import Register as RegisterEvents

from Modules.Config.Config  import VERSION
from Modules.Shared.Objects import Release


intents = Discord.Intents.all()

BOT = Commands.AutoShardedBot(intents=intents, description="Test", command_prefix=Random.random().__str__())

BOT.remove_command("help")

RegisterCommands(BOT)
RegisterEvents  (BOT)

if VERSION.release == Release.STABLE:
    BOT.run(DotEnv.get_key(Pathlib.Path(__file__).parent.joinpath("./.env"), "TOKEN"))
else:
    BOT.run(DotEnv.get_key(Pathlib.Path(__file__).parent.joinpath("./.env"), "TOKEN_DEV"))
