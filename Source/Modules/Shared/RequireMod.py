import discord
from Modules.Config import Embed

async def RequireMod(ctx: discord.ApplicationContext):
    """
    This function will return `True` IF the user is a mod, else it responds
    Usage: `if not await RequireMod(ctx): return`
    """
    if ctx.author.guild_permissions.manage_guild:
        return True
    else:
        await ctx.respond(embed=Embed.REQUIRES_MOD, ephemeral=True)
        return False

async def RequireModNE(ctx: discord.ApplicationContext):
    """
    This function will return `True` IF the user is a mod, else it responds
    Usage: `if not await RequireMod(ctx): return`
    NOTE: This version doesn't use ephemeral, so it can be used in a normal message
    Use `RequireMod` if you want to use ephemeral (so it doesn't show up in the channel for everyone)
    """
    if ctx.author.guild_permissions.manage_guild:
        return True
    else:
        await ctx.respond(embed=Embed.REQUIRES_MOD, ephemeral=False)
        return False