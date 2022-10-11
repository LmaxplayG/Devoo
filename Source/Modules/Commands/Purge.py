import discord
from discord.ext import commands
import copy
from Modules.Config import Embed
from Modules.Shared import RequireMod

class Purge(discord.Cog):
    @discord.slash_command(description="Purges N amount of messages from the channel")
    async def purge(self, ctx: discord.ApplicationContext, amount: int):
        if not await RequireMod(ctx): return
        await ctx.defer()
        if amount > 100:
            await ctx.respond(embed=Embed.PURGE_MAX_AMOUNT)
            return
        await ctx.channel.purge(limit=amount)
        embed = copy.deepcopy(Embed.PURGE)
        embed.description = embed.description.replace("{AMOUNT}", str(amount))
        await ctx.send(embed=embed, ephemeral=True)