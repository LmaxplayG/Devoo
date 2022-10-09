import discord
from discord.ext import commands
import copy
from Modules.Config import Embed

class Site(commands.Cog):
    @commands.slash_command(description="")
    async def site(self, ctx: discord.ApplicationContext):
        embed = copy.copy(Embed.SITE)
        await ctx.respond(embed=embed, ephemeral=True)