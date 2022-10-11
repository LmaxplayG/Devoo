import discord
from discord.ext import commands
import copy
from Modules.Config import Embed
from Modules.Shared import RequireMod

class About(discord.Cog):
    @commands.slash_command(description="Info about the bot")
    async def about(self, ctx: discord.ApplicationContext):
        embed = copy.deepcopy(Embed.ABOUT)
        await ctx.respond(embed=embed, ephemeral=True)

    @commands.slash_command(description="Gives a link to this bots site")
    async def site(self, ctx: discord.ApplicationContext):
        embed = copy.deepcopy(Embed.SITE)
        await ctx.respond(embed=embed, ephemeral=True)
    
    @commands.slash_command(description="Gives a link to this bots source code")
    async def source(self, ctx: discord.ApplicationContext):
        embed = copy.deepcopy(Embed.SOURCE)
        await ctx.respond(embed=embed, ephemeral=True)

    @commands.slash_command(description="Gives a link to this bots support server")
    async def support(self, ctx: discord.ApplicationContext):
        embed = copy.deepcopy(Embed.SUPPORT)
        await ctx.respond(embed=embed, ephemeral=True)
