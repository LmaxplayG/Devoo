from discord.ext import commands

from . import Moderation, About, Random, Site

def Register(bot: commands.Bot):
    bot.add_cog(Moderation.Moderation())
    bot.add_cog(Random.Random())
    bot.add_cog(About.About())
    bot.add_cog(Site.Site())