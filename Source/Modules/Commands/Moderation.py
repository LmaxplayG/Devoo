import datetime
import discord
from discord.ext import commands
import copy
from Modules.Config import Embed
from Modules.Shared import RequireMod

class Moderation(commands.Cog):
    @commands.slash_command(description="Kicks a user from the server")
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx: discord.ApplicationContext, member: discord.Member, reason: str = 'No reason specified'):
        await ctx.defer(ephemeral=True)
        if not await RequireMod(ctx): return
        if member.bot:
            await ctx.followup.send(embed=Embed.CANNOT_KICK_BOT, ephemeral=True)
            return
        if ctx.author.top_role.position < member.top_role.position:
            embed = copy.deepcopy(Embed.ROLE_ABOVE)
            embed.description = embed.description.replace(
                '{USERNAME}', member.name)
            await ctx.followup.send(embed=embed, ephemeral=True)
        embed = copy.deepcopy(Embed.MEMBER_KICK_DM)
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
            embed = copy.deepcopy(Embed.KICK_ERROR_GENERIC)
            embed.description = embed.description.replace('{USERNAME}', member.mention)
            await ctx.followup.send(embed=embed, ephemeral=True)
            return
        embed = copy.deepcopy(Embed.MEMBER_KICK)
        embed.description = embed.description.replace(
            '{MEMBER}', f"{member.name}#{member.discriminator}").replace('{REASON}', reason)
        await ctx.followup.send(embed=embed, ephemeral=True)

    @commands.slash_command(description="Bans a user from the server")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx: discord.ApplicationContext, member: discord.Member, reason: str = 'No reason specified'):
        await ctx.defer(ephemeral=True)
        req = await RequireMod(ctx)
        if req:
            return
        if member.bot:
            await ctx.followup.send(embed=Embed.CANNOT_BAN_BOT, ephemeral=True)
            return
        if ctx.author.top_role.position < member.top_role.position:
            embed = copy.deepcopy(Embed.ROLE_ABOVE)
            embed.description = embed.description.replace(
                '{USERNAME}', member.name)
            await ctx.followup.send(embed=embed, ephemeral=True)
        embed = copy.deepcopy(Embed.MEMBER_BAN_DM)
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
            embed = copy.deepcopy(Embed.BAN_ERROR_GENERIC)
            embed.description = embed.description.replace('{USERNAME}', member.mention)
            await ctx.followup.send(embed=embed, ephemeral=True)
            return
        embed = copy.deepcopy(Embed.MEMBER_BAN)
        embed.description = embed.description.replace(
            '{MEMBER}', f"{member.name}#{member.discriminator}").replace('{REASON}', reason)
        await ctx.followup.send(embed=embed, ephemeral=True)

    @commands.slash_command(description="Times out a user")
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def timeout(self, ctx: discord.ApplicationContext, member: discord.Member, seconds: int = 0, minutes: int = 0, hours: int = 0, days: int = 0, reason: str = 'No reason specified'):
        await ctx.defer(ephemeral=True)
        req = await RequireMod(ctx)
        if req:
            return
        if member.bot:
            await ctx.followup.send(embed=Embed.ERROR_CANNOT_TIMEOUT_BOT, ephemeral=True)
            return
        if ctx.author.top_role.position < member.top_role.position:
            embed = copy.deepcopy(Embed.ROLE_ABOVE)
            embed.description = embed.description.replace(
                '{USERNAME}', member.name)
            await ctx.followup.send(embed=embed, ephemeral=True)
        embed = copy.deepcopy(Embed.MEMBER_TIMEOUT_DM)
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
            embed = copy.deepcopy(Embed.TIMEOUT_ERROR_GENERIC)
            embed.description = embed.description.replace('{USERNAME}', member.mention)
            await ctx.followup.send(embed=embed, ephemeral=True)
            return
        embed = copy.deepcopy(Embed.MEMBER_TIMEOUT)
        embed.description = embed.description.replace('{MEMBER}', f"{member.name}#{member.discriminator}").replace(
            '{REASON}', reason).replace('{TIME}', datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds).__str__())
        await ctx.followup.send(embed=embed, ephemeral=True)

    @discord.slash_command(description="Purges N amount of messages from the channel")
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx: discord.ApplicationContext, amount: int):
        await ctx.defer(ephemeral=True)
        if not await RequireMod(ctx): return
        if amount > 100:
            await ctx.followup.send(embed=Embed.PURGE_MAX_AMOUNT)
            return
        await ctx.channel.purge(limit=amount)
        embed = copy.deepcopy(Embed.PURGE)
        embed.description = embed.description.replace("{AMOUNT}", str(amount))
        await ctx.send(embed=embed, ephemeral=True)
    
    @discord.slash_command(description="Mutes a user")
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx: discord.ApplicationContext, member: discord.Member, reason: str = 'No reason specified'):
        await ctx.defer(ephemeral=True)
        if not await RequireMod(ctx): return
        if member.bot:
            await ctx.followup.send(embed=Embed.ERROR_CANNOT_MUTE_BOT, ephemeral=True)
            return
        if ctx.author.top_role.position < member.top_role.position:
            embed = copy.deepcopy(Embed.ROLE_ABOVE)
            embed.description = embed.description.replace(
                '{USERNAME}', member.name)
            await ctx.followup.send(embed=embed, ephemeral=True)

        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not mute_role:
            await ctx.followup.send(embed=Embed.MUTE_ROLE_NOT_FOUND, ephemeral=True)
            return
        
        try:
            await member.add_roles(mute_role)
        except:
            await ctx.followup.send(embed=Embed.MUTE_ERROR_GENERIC, ephemeral=True)
            return
        
        embed = copy.deepcopy(Embed.MEMBER_MUTE)
        embed.description = embed.description.replace('{MEMBER}', f"{member.name}#{member.discriminator}").replace(
            '{REASON}', reason)
        await ctx.followup.send(embed=embed, ephemeral=True)