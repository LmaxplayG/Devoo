import datetime
import discord
from discord.ext import commands
import copy
from Modules.Config import Config, Embed
from Modules.Shared import RequireMod

class Moderation(commands.Cog):
    @commands.slash_command(description="Kicks a user from the server")
    async def kick(self, ctx: discord.ApplicationContext, member: discord.Member, reason: str = 'No reason specified'):
        req = await RequireMod(ctx)
        if req:
            return
        if member.bot:
            await ctx.respond(embed=Embed.ERROR_CANNOT_KICK_BOT, ephemeral=True)
            return
        if ctx.author.top_role.position < member.top_role.position:
            embed = copy.copy(Embed.ROLE_ABOVE)
            embed.description = embed.description.replace(
                '{USERNAME}', member.name)
            await ctx.respond(embed=embed, ephemeral=True)
        embed = copy.copy(Embed.MEMBER_KICK_DM)
        embed.title = embed.title.replace(
            '{SERVERNAME}', ctx.guild.name).replace('{REASON}', reason)
        embed.description = embed.description.replace(
            '{SERVERNAME}', ctx.guild.name).replace('{REASON}', reason)
        try:
            await member.send(embed=embed)
        except:
            ""
        try:
            await member.kick(reason=reason)
        except:
            embed = copy.copy(Embed.ERROR_KICK)
            embed.description = embed.description.replace('{USERNAME}', member)
            await ctx.respond(embed=embed, ephemeral=True)
            return
        embed = copy.copy(Embed.MEMBER_KICK)
        embed.description = embed.description.replace(
            '{MEMBER}', f"{member.name}#{member.discriminator}").replace('{REASON}', reason)
        await ctx.respond(embed=embed, ephemeral=True)

    @commands.slash_command(description="Bans a user from the server")
    async def ban(self, ctx: discord.ApplicationContext, member: discord.Member, reason: str = 'No reason specified'):
        req = await RequireMod(ctx)
        if req:
            return
        if member.bot:
            await ctx.respond(embed=Embed.ERROR_CANNOT_BAN_BOT, ephemeral=True)
            return
        if ctx.author.top_role.position < member.top_role.position:
            embed = copy.copy(Embed.ROLE_ABOVE)
            embed.description = embed.description.replace(
                '{USERNAME}', member.name)
            await ctx.respond(embed=embed, ephemeral=True)
        embed = copy.copy(Embed.MEMBER_BAN_DM)
        embed.title = embed.title.replace(
            '{SERVERNAME}', ctx.guild.name).replace('{REASON}', reason)
        embed.description = embed.description.replace(
            '{SERVERNAME}', ctx.guild.name).replace('{REASON}', reason)
        try:
            await member.send(embed=embed)
        except:
            ""
        try:
            await member.ban(reason=reason)
        except:
            embed = copy.copy(Embed.ERROR_BAN)
            embed.description = embed.description.replace('{USERNAME}', member)
            await ctx.respond(embed=embed, ephemeral=True)
            return
        embed = copy.copy(Embed.MEMBER_BAN)
        embed.description = embed.description.replace(
            '{MEMBER}', f"{member.name}#{member.discriminator}").replace('{REASON}', reason)
        await ctx.respond(embed=embed, ephemeral=True)

    @commands.slash_command(description="Times out a user")
    async def timeout(self, ctx: discord.ApplicationContext, member: discord.Member, seconds: int = 0, minutes: int = 0, hours: int = 0, days: int = 0, reason: str = 'No reason specified'):
        req = await RequireMod(ctx)
        if req:
            return
        if member.bot:
            await ctx.respond(embed=Embed.ERROR_CANNOT_TIMEOUT_BOT, ephemeral=True)
            return
        if ctx.author.top_role.position < member.top_role.position:
            embed = copy.copy(Embed.ROLE_ABOVE)
            embed.description = embed.description.replace(
                '{USERNAME}', member.name)
            await ctx.respond(embed=embed, ephemeral=True)
        embed = copy.copy(Embed.MEMBER_TIMEOUT_DM)
        embed.title = embed.title.replace(
            '{SERVERNAME}', ctx.guild.name).replace('{REASON}', reason)
        embed.description = embed.description.replace('{SERVERNAME}', ctx.guild.name).replace('{REASON}', reason).replace(
            '{TIME}', datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds).__str__())
        try:
            await member.send(embed=embed)
        except:
            ""
        try:
            await member.timeout_for(reason=reason, duration=datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds))
        except:
            embed = copy.copy(Embed.ERROR_TIMEOUT)
            embed.description = embed.description.replace('{USERNAME}', member)
            await ctx.respond(embed=embed, ephemeral=True)
            return
        embed = copy.copy(Embed.MEMBER_TIMEOUT)
        embed.description = embed.description.replace('{MEMBER}', f"{member.name}#{member.discriminator}").replace(
            '{REASON}', reason).replace('{TIME}', datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds).__str__())
        await ctx.respond(embed=embed, ephemeral=True)
