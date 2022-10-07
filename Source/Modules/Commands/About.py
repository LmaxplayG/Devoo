import datetime
import discord
from discord.ext import commands
import copy
from Modules.Config import Config
from Modules.Shared import RequireMod

class About(discord.Cog):
    @commands.slash_command(description="Info about the bot")
    async def about(self, ctx: discord.ApplicationContext):
        embed = copy.copy(Config.EMBED_ABOUT)
        await ctx.respond(embed=embed, ephemeral=True)
