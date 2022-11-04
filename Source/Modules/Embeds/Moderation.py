
import discord as Discord

from Modules.Config import Color



class KickEmbeds:
    """
    Embeds for /kick
    """
    async def kick_embed(moderator: Discord.Member, member: Discord.Member, reason: str):
        embed = Discord.Embed(color=Color.PRIMARY, title="Kick", description=f"""\
        {member.mention} was kicked by {moderator.mention}
        Reason:
        ```
        {reason}
        ```\
        """)
        embed.set_thumbnail(url=member.avatar.url)
        return embed

    async def kick_embed_dm(moderator: Discord.Member, member: Discord.Member, reason: str):
        embed = Discord.Embed(color=Color.PRIMARY, title="Kick", description=f"""\
        You were kicked from {member.guild.name}
        Reason:
        ```
        {reason}
        ```\
        """)
        embed.set_thumbnail(url=member.avatar.url)
        return embed
    
    async def kick_cannot_kick_bot():
        return Discord.Embed(color=Color.ERROR, title="Error", description="""\
        You cannot kick bots\
        """)

    async def kick_role_above():
        return Discord.Embed(color=Color.ERROR, title="Error", description="""\
        You cannot kick someone with a role above you\
        """)

    async def kick_error_generic():
        return Discord.Embed(color=Color.ERROR, title="Error", description="""\
        I was unable to kick the user\
        """)



class BanEmbeds:
    """
    Embeds for /ban
    """
    async def ban_embed(moderator: Discord.Member, member: Discord.Member, reason: str):
        embed = Discord.Embed(color=Color.PRIMARY, title="Ban", description=f"""\
        {member.mention} was banned by {moderator.mention}
        Reason:
        ```
        {reason}
        ```\
        """)
        embed.set_thumbnail(url=member.avatar.url)
        return embed

    async def ban_embed_dm(moderator: Discord.Member, member: Discord.Member, reason: str):
        embed = Discord.Embed(color=Color.PRIMARY, title="Ban", description=f"""\
        You were banned from {member.guild.name}
        Reason:
        ```
        {reason}
        ```\
        """)
        embed.set_thumbnail(url=member.avatar.url)
        return embed

    async def ban_cannot_ban_bot():
        return Discord.Embed(color=Color.ERROR, title="Error", description="""\
        You cannot ban bots\
        """)

    async def ban_role_above():
        return Discord.Embed(color=Color.ERROR, title="Error", description="""\
        You cannot ban someone with a role above you\
        """)

    async def ban_error_generic():
        return Discord.Embed(color=Color.ERROR, title="Error", description="""\
        I was unable to ban the user\
        """)



class TimeoutEmbeds:
    """
    Embeds for /timeout
    """
    async def embed(moderator: Discord.Member, member: Discord.Member, reason: str):
        embed = Discord.Embed(color=Color.PRIMARY, title="Timeout", description=f"""\
        {member.mention} was timed out by {moderator.mention}
        Reason:
        ```
        {reason}
        ```\
        """)
        embed.set_thumbnail(url=member.avatar.url)
        return embed

    async def embed_dm(moderator: Discord.Member, member: Discord.Member, reason: str):
        embed = Discord.Embed(color=Color.PRIMARY, title="Timeout", description=f"""\
        You were timed out from {member.guild.name}
        Reason:
        ```
        {reason}
        ```\
        """)
        embed.set_thumbnail(url=member.avatar.url)
        return embed

    async def cannot_timeout_bot():
        return Discord.Embed(color=Color.ERROR, title="Error", description="""\
        You cannot timeout bots\
        """)

    async def role_above():
        return Discord.Embed(color=Color.ERROR, title="Error", description="""\
        You cannot timeout someone with a role above you\
        """)

    async def error_generic():
        return Discord.Embed(color=Color.ERROR, title="Error", description="""\
        I was unable to timeout the user\
        """)



class PurgeEmbeds:
    """
    Embeds for /purge
    """
    async def purge_embed(moderator: Discord.Member, amount: int):
        embed = Discord.Embed(color=Color.PRIMARY, title="Purge", description=f"""\
        {amount} messages were purged by {moderator.mention}\
        """)
        return embed

    async def error_generic():
        return Discord.Embed(color=Color.ERROR, title="Error", description="""\
        I was unable to purge the messages\
        """)
    
    async def purge_too_many(amount: int):
        return Discord.Embed(color=Color.ERROR, title="Error", description=f"""\
        You cannot purge more than {amount} messages\
        """)