import datetime             as DateTime
import discord              as Discord
import discord.ext.commands as Commands
import copy                 as Copy

from Modules.Embeds.Moderation import KickEmbeds, BanEmbeds, TimeoutEmbeds, PurgeEmbeds

class Moderation(Commands.Cog):
    @Commands.slash_command(description="Kicks a user from the server")
    @Commands.guild_only()
    @Commands.has_permissions(kick_members=True)
    async def kick(self, ctx: Discord.ApplicationContext, member: Discord.Member, reason: str = 'No reason specified'):
        await ctx.defer(ephemeral=True)
        if member.bot:
            await ctx.followup.send(embed=KickEmbeds.kick_cannot_kick_bot(), ephemeral=True)
            return
        if ctx.author.top_role.position < member.top_role.position:
            await ctx.followup.send(embed=KickEmbeds.kick_role_above(), ephemeral=True)
        try:
            await member.send(embed=KickEmbeds.kick_embed_dm(ctx.author, member, reason))
        except:
            pass
        try:
            await member.kick(reason=reason)
        except:
            await ctx.followup.send(embed=KickEmbeds.kick_error_generic(), ephemeral=True)
            return
        await ctx.followup.send(embed=KickEmbeds.kick_embed(ctx.author, member, reason), ephemeral=True)


    @Commands.slash_command(description="Bans a user from the server")
    @Commands.guild_only()
    @Commands.has_permissions(ban_members=True)
    async def ban(self, ctx: Discord.ApplicationContext, member: Discord.Member, reason: str = 'No reason specified'):
        await ctx.defer(ephemeral=True)
        if member.bot:
            await ctx.followup.send(embed=BanEmbeds.ban_cannot_ban_bot(), ephemeral=True)
            return
        if ctx.author.top_role.position < member.top_role.position:
            await ctx.followup.send(embed=BanEmbeds.ban_role_above(), ephemeral=True)
        try:
            await member.send(embed=BanEmbeds.ban_embed_dm(ctx.author, member, reason))
        except:
            pass
        try:
            await member.ban(reason=reason)
        except:
            await ctx.followup.send(embed=BanEmbeds.ban_error_generic(), ephemeral=True)
            return
        await ctx.followup.send(embed=BanEmbeds.ban_embed(ctx.author, member, reason), ephemeral=True)


    @Commands.slash_command(description="Timeouts a user from the server")
    @Commands.guild_only()
    @Commands.has_permissions(manage_messages=True)
    async def timeout(self, ctx: Discord.ApplicationContext, member: Discord.Member, reason: str = 'No reason specified'):
        await ctx.defer(ephemeral=True)
        if member.bot:
            await ctx.followup.send(embed=TimeoutEmbeds.cannot_timeout_bot(), ephemeral=True)
            return
        if ctx.author.top_role.position < member.top_role.position:
            await ctx.followup.send(embed=TimeoutEmbeds.role_above(), ephemeral=True)
        try:
            await member.send(embed=TimeoutEmbeds.embed_dm(ctx.author, member, reason))
        except:
            pass
        try:
            await member.timeout(reason=reason)
        except:
            await ctx.followup.send(embed=TimeoutEmbeds.error_generic(), ephemeral=True)
            return
        await ctx.followup.send(embed=TimeoutEmbeds.embed(ctx.author, member, reason), ephemeral=True)



    @Discord.slash_command(description="Purges N amount of messages from the channel")
    @Commands.guild_only()
    @Commands.has_permissions(manage_messages=True)
    async def purge(self, ctx: Discord.ApplicationContext, amount: int):
        await ctx.defer(ephemeral=True)
        if amount > 100:
            await ctx.followup.send(embed=PurgeEmbeds.purge_too_many(), ephemeral=True)
            return
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=PurgeEmbeds.purge_embed(ctx.author, amount), ephemeral=True)