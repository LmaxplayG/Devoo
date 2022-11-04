import discord as Discord

from Modules.Config import Color

class PermissionEmbeds:
    async def missing_permissions_embed():
        return Discord.Embed(color=Color.ERROR, title="Error", description="""\
        I am missing permissions to do this\
        """)

MEMBER_MISSING_PERMISSIONS = Discord.Embed(color=Color.ERROR, title="Error", description="""\
You need `{PERMISSION}` to do this\
""")
