import discord
from Modules.Config import Config

async def RequireMod(ctx: discord.ApplicationContext):
    """
    This function will return `True` IF the user is a mod, else it responds
    """
    if not ctx.author.guild_permissions.kick_members\
            and not ctx.author.guild_permissions.ban_members\
            and not ctx.author.guild_permissions.manage_messages:
        await ctx.respond(embed=Config.EMBED_REQUIRES_MOD)
        return True
    else:
        return False