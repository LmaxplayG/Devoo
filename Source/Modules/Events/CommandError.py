from discord.ext import commands
import copy
import discord
from Modules.Config import Embed, Color

async def on_command_error(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.CommandNotFound):
        # ,  description=f"Command  not found")
        embed = discord.Embed(color=Color.ERROR, title="Command not found")
        await ctx.send(embed=embed)
        return
    elif isinstance(error, commands.CommandInvokeError):
        embed = copy.deepcopy(Embed.ERROR)
        embed.description = embed.description.replace('{ERR}', str(error))
        await ctx.send(embed=embed)
        return
    elif isinstance(error, commands.MissingRequiredArgument):
        errStr = error.args[0].replace(
            ' is a required argument that is missing.', '')
        embed = discord.Embed(color=Color.ERROR, title="A required argument is missing",
                              description=f"Please give a value for `{errStr}`")
        await ctx.send(embed=embed)
        return
    embed = discord.Embed(color=Color.ERROR, title="An error occured",
                          description=f"```py\n{str(error)}\n```")
    await ctx.send(embed=embed)
    await ctx.message.add_reaction("⚠️")

async def on_slash_command_error(ctx: discord.ApplicationContext, error: commands.CommandError):
    # Defer if we haven't already
    try:
        await ctx.defer(ephemeral=True)
    except:
        ""
    if isinstance(error, commands.NoPrivateMessage):
        embed = copy.deepcopy(Embed.UNAVAILABLE_IN_DMS)
        await ctx.respond(embed=embed, ephemeral=True)
        return
    elif isinstance(error, commands.MissingPermissions):
        embed = copy.deepcopy(Embed.MEMBER_MISSING_PERMISSIONS)
        embed.description = embed.description.replace(
            '{PERMISSION}', error.missing_perms[0])
        await ctx.respond(embed=embed, ephemeral=True)
        return
    elif isinstance(error, commands.BotMissingPermissions):
        embed = copy.deepcopy(Embed.BOT_MISSING_PERMISSIONS)
        embed.description = embed.description.replace(
            '{PERMISSION}', error.missing_perms[0])
        # We check if we have already responded to the user, if not we respond, else we edit the response
        if ctx.response.is_done():
            await ctx.edit_response(embed=embed)
        else:
            await ctx.respond(embed=embed)
        return
    else :
        embed = copy.deepcopy(Embed.ERROR)
        embed.description = embed.description.replace('{ERR}', str(error))
        if ctx.response.is_done():
            await ctx.response.edit_message(embed=embed)
        else:
            await ctx.respond(embed=embed)
        return