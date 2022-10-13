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
    await ctx.defer(ephemeral=True)
    if isinstance(error, commands.NoPrivateMessage):
        embed = copy.deepcopy(Embed.NO_DM)
        await ctx.respond(embed=embed, ephemeral=True)
        return