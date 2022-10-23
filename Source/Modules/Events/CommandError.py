import discord as Discord
import discord.ext.commands as Commands
import copy as Copy

import Modules.Config.Color as Color
import Modules.Config.Embed as Embed

async def on_command_error(ctx: Commands.Context, error: Commands.CommandError):
    if isinstance(error, Commands.CommandNotFound):
        # ,  description=f"Command  not found")
        embed = Discord.Embed(color=Color.ERROR, title="Command not found")
        await ctx.send(embed=embed)
        return
    elif isinstance(error, Commands.CommandInvokeError):
        embed = Copy.deepcopy(Embed.ERROR)
        embed.description = embed.description.replace('{ERR}', str(error))
        await ctx.send(embed=embed)
        return
    elif isinstance(error, Commands.MissingRequiredArgument):
        errStr = error.args[0].replace(
            ' is a required argument that is missing.', '')
        embed = Discord.Embed(color=Color.ERROR, title="A required argument is missing",
                              description=f"Please give a value for `{errStr}`")
        await ctx.send(embed=embed)
        return
    embed = Discord.Embed(color=Color.ERROR, title="An error occured",
                          description=f"```py\n{str(error)}\n```")
    await ctx.send(embed=embed)
    await ctx.message.add_reaction("⚠️")

async def on_slash_command_error(ctx: Discord.ApplicationContext, error: Commands.CommandError):
    # Defer if we haven't already
    try:
        await ctx.defer(ephemeral=True)
    except:
        ""
    if isinstance(error, Commands.NoPrivateMessage):
        embed = Copy.deepcopy(Embed.UNAVAILABLE_IN_DMS)
        await ctx.respond(embed=embed, ephemeral=True)
        return
    elif isinstance(error, Commands.MissingPermissions):
        embed = Copy.deepcopy(Embed.MEMBER_MISSING_PERMISSIONS)
        embed.description = embed.description.replace(
            '{PERMISSION}', error.missing_perms[0])
        await ctx.respond(embed=embed, ephemeral=True)
        return
    elif isinstance(error, Commands.BotMissingPermissions):
        embed = Copy.deepcopy(Embed.BOT_MISSING_PERMISSIONS)
        embed.description = embed.description.replace(
            '{PERMISSION}', error.missing_perms[0])
        # We check if we have already responded to the user, if not we respond, else we edit the response
        if ctx.response.is_done():
            await ctx.edit_response(embed=embed)
        else:
            await ctx.respond(embed=embed)
        return
    else :
        embed = Copy.deepcopy(Embed.ERROR)
        embed.description = embed.description.replace('{ERR}', str(error))
        if ctx.response.is_done():
            await ctx.response.edit_message(embed=embed)
        else:
            await ctx.respond(embed=embed)
        return