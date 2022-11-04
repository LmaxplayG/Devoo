import discord as Discord
import discord.ext.commands as Commands
import copy as Copy

import Modules.Config.Color as Color
from Modules.Embeds.Events import SlashCommandErrorEmbeds

async def on_slash_command_error(ctx: Discord.ApplicationContext, error: Commands.CommandError):
    # Defer if we haven't already
    try:
        await ctx.defer(ephemeral=True)
    except:
        pass
    if isinstance(error, Commands.NoPrivateMessage):
        await ctx.respond(embed=SlashCommandErrorEmbeds.no_private_message(), ephemeral=True)
        return
    elif isinstance(error, Commands.MissingPermissions):
        await ctx.respond(embed=SlashCommandErrorEmbeds.missing_permissions_embed(error.missing_permissions), ephemeral=True)
        return
    elif isinstance(error, Commands.BotMissingPermissions):
        embed = SlashCommandErrorEmbeds.missing_permissions_embed_bot(error.missing_permissions)
        if ctx.response.is_done():
            await ctx.edit_response(embed=embed)
        else:
            await ctx.respond(embed=embed)
        return
    else :
        embed = SlashCommandErrorEmbeds.slash_command_error_embed(error)
        if not ctx.response.is_done():
            await ctx.response.edit_message(embed=embed)
        else:
            await ctx.respond(embed=embed)
        return