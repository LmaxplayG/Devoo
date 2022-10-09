import datetime
from re import L
import discord
from discord.ext import commands
import copy
from Modules.Config import Config, Embed
from Modules.Shared import RequireMod
import secrets

class Site(commands.Cog):
    @commands.slash_command(description="")
    async def site(self, ctx: discord.ApplicationContext):
        embed = copy.copy(Embed.SITE)
        await ctx.respond(embed=embed, ephemeral=True)