from discord.ext import commands

from .Moderation import Moderation
from .Random import Random
from .About import About

def Register(bot: commands.Bot):
    bot.add_cog(Moderation())
    bot.add_cog(Random())
    bot.add_cog(About())