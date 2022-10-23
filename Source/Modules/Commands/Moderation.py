import datetime             as DateTime
import discord              as Discord
import discord.ext.commands as Commands
import copy                 as Copy

import Modules.Config.Embed as Embed

class Moderation(Commands.Cog):
    @Commands.slash_command(description="Kicks a user from the server")
    @Commands.guild_only()
    @Commands.has_permissions(kick_members=True)
    async def kick(self, ctx: Discord.ApplicationContext, member: Discord.Member, reason: str = 'No reason specified'):
        await ctx.defer(ephemeral=True)
        if member.bot:
            await ctx.followup.send(embed=Embed.CANNOT_KICK_BOT, ephemeral=True)
            return
        if ctx.author.top_role.position < member.top_role.position:
            embed = Copy.deepcopy(Embed.ROLE_ABOVE)
            embed.description = embed.description.replace(
                '{USERNAME}', member.name)
            await ctx.followup.send(embed=embed, ephemeral=True)
        embed = Copy.deepcopy(Embed.MEMBER_KICK_DM)
        embed.title = embed.title.replace(
            '{SERVERNAME}', ctx.guild.name).replace('{REASON}', reason)
        embed.description = embed.description.replace(
            '{SERVERNAME}', ctx.guild.name).replace('{REASON}', reason)
        try:
            await member.send(embed=embed)
        except:
            pass
        try:
            await member.kick(reason=reason)
        except:
            embed = Copy.deepcopy(Embed.KICK_ERROR_GENERIC)
            embed.description = embed.description.replace('{USERNAME}', member.mention)
            await ctx.followup.send(embed=embed, ephemeral=True)
            return
        embed = Copy.deepcopy(Embed.MEMBER_KICK)
        embed.description = embed.description.replace(
            '{MEMBER}', f"{member.name}#{member.discriminator}").replace('{REASON}', reason)
        await ctx.followup.send(embed=embed, ephemeral=True)

    @Commands.slash_command(description="Bans a user from the server")
    @Commands.guild_only()
    @Commands.has_permissions(ban_members=True)
    async def ban(self, ctx: Discord.ApplicationContext, member: Discord.Member, reason: str = 'No reason specified'):
        await ctx.defer(ephemeral=True)
        if member.bot:
            await ctx.followup.send(embed=Embed.CANNOT_BAN_BOT, ephemeral=True)
            return
        if ctx.author.top_role.position < member.top_role.position:
            embed = Copy.deepcopy(Embed.ROLE_ABOVE)
            embed.description = embed.description.replace(
                '{USERNAME}', member.name)
            await ctx.followup.send(embed=embed, ephemeral=True)
        embed = Copy.deepcopy(Embed.MEMBER_BAN_DM)
        embed.title = embed.title.replace(
            '{SERVERNAME}', ctx.guild.name).replace('{REASON}', reason)
        embed.description = embed.description.replace(
            '{SERVERNAME}', ctx.guild.name).replace('{REASON}', reason)
        try:
            await member.send(embed=embed)
        except:
            pass
        try:
            await member.ban(reason=reason)
        except:
            embed = Copy.deepcopy(Embed.BAN_ERROR_GENERIC)
            embed.description = embed.description.replace('{USERNAME}', member.mention)
            await ctx.followup.send(embed=embed, ephemeral=True)
            return
        embed = Copy.deepcopy(Embed.MEMBER_BAN)
        embed.description = embed.description.replace(
            '{MEMBER}', f"{member.name}#{member.discriminator}").replace('{REASON}', reason)
        await ctx.followup.send(embed=embed, ephemeral=True)

    @Commands.slash_command(description="Times out a user")
    @Commands.guild_only()
    @Commands.has_permissions(manage_messages=True)
    async def timeout(self, ctx: Discord.ApplicationContext, member: Discord.Member, seconds: int = 0, minutes: int = 0, hours: int = 0, days: int = 0, reason: str = 'No reason specified'):
        await ctx.defer(ephemeral=True)
        if member.bot:
            await ctx.followup.send(embed=Embed.ERROR_CANNOT_TIMEOUT_BOT, ephemeral=True)
            return
        if ctx.author.top_role.position < member.top_role.position:
            embed = Copy.deepcopy(Embed.ROLE_ABOVE)
            embed.description = embed.description.replace(
                '{USERNAME}', member.name)
            await ctx.followup.send(embed=embed, ephemeral=True)
        embed = Copy.deepcopy(Embed.MEMBER_TIMEOUT_DM)
        embed.title = embed.title.replace(
            '{SERVERNAME}', ctx.guild.name).replace('{REASON}', reason)
        embed.description = embed.description.replace('{SERVERNAME}', ctx.guild.name).replace('{REASON}', reason).replace(
            '{TIME}', DateTime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds).__str__())
        try:
            await member.send(embed=embed)
        except:
            pass
        try:
            await member.timeout_for(reason=reason, duration=DateTime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds))
        except:
            embed = Copy.deepcopy(Embed.TIMEOUT_ERROR_GENERIC)
            embed.description = embed.description.replace('{USERNAME}', member.mention)
            await ctx.followup.send(embed=embed, ephemeral=True)
            return
        embed = Copy.deepcopy(Embed.MEMBER_TIMEOUT)
        embed.description = embed.description.replace('{MEMBER}', f"{member.name}#{member.discriminator}").replace(
            '{REASON}', reason).replace('{TIME}', DateTime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds).__str__())
        await ctx.followup.send(embed=embed, ephemeral=True)

    @Discord.slash_command(description="Purges N amount of messages from the channel")
    @Commands.guild_only()
    @Commands.has_permissions(manage_messages=True)
    async def purge(self, ctx: Discord.ApplicationContext, amount: int):
        await ctx.defer(ephemeral=True)
        if amount > 100:
            await ctx.followup.send(embed=Embed.PURGE_MAX_AMOUNT)
            return
        await ctx.channel.purge(limit=amount)
        embed = Copy.deepcopy(Embed.PURGE)
        embed.description = embed.description.replace("{AMOUNT}", str(amount))
        await ctx.send(embed=embed, ephemeral=True)
    
    @Discord.slash_command(description="Mutes a user")
    @Commands.guild_only()
    @Commands.has_permissions(manage_messages=True)
    async def mute(self, ctx: Discord.ApplicationContext, member: Discord.Member, reason: str = 'No reason specified'):
        await ctx.defer(ephemeral=True)
        if member.bot:
            await ctx.followup.send(embed=Embed.ERROR_CANNOT_MUTE_BOT, ephemeral=True)
            return
        if ctx.author.top_role.position < member.top_role.position:
            embed = Copy.deepcopy(Embed.ROLE_ABOVE)
            embed.description = embed.description.replace(
                '{USERNAME}', member.name)
            await ctx.followup.send(embed=embed, ephemeral=True)

        mute_role = Discord.utils.get(ctx.guild.roles, name="Muted")
        if not mute_role:
            await ctx.followup.send(embed=Embed.MUTE_ROLE_NOT_FOUND, ephemeral=True)
            return
        
        try:
            await member.add_roles(mute_role)
        except:
            await ctx.followup.send(embed=Embed.MUTE_ERROR_GENERIC, ephemeral=True)
            return
        
        embed = Copy.deepcopy(Embed.MEMBER_MUTE)
        embed.description = embed.description.replace('{MEMBER}', f"{member.name}#{member.discriminator}").replace(
            '{REASON}', reason)
        await ctx.followup.send(embed=embed, ephemeral=True)