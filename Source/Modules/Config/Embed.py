
import discord
from sys import version
from . import Color, Config

# Embeds
REQUIRES_PREMIUM = discord.Embed(color=Color.ERROR, title="You don't have permission", description="""\
This command requires premium!!!
Buy at https://devoopers.net/premium\
""")


REQUIRES_MOD = discord.Embed(color=Color.ERROR, title="You don't have permission", description="""\
This requires moderator permissions\
""")




MEMBER_KICK = discord.Embed(color=Color.PRIMARY, title="Member kicked", description="""\
Kicked {MEMBER} with the reason
```
{REASON}
```\
""")

MEMBER_KICK_DM = discord.Embed(color=Color.PRIMARY, title="You were kicked from {SERVERNAME}", description="""\
You were kicked from {SERVERNAME} with the reason
```
{REASON}
```\
""")



MEMBER_BAN = discord.Embed(color=Color.PRIMARY, title="Member kicked", description="""\
Kicked {MEMBER} with the reason
```
{REASON}
```\
""")

MEMBER_BAN_DM = discord.Embed(color=Color.PRIMARY, title="You were kicked from {SERVERNAME}", description="""\
You were kicked from {SERVERNAME} with the reason
```
{REASON}
```\
""")



MEMBER_TIMEOUT = discord.Embed(color=Color.PRIMARY, title="Member timed out", description="""\
Timed out {MEMBER} for {TIME} with the reason
```
{REASON}
```\
""")

MEMBER_TIMEOUT_DM = discord.Embed(color=Color.PRIMARY, title="You were timed out on {SERVERNAME}", description="""\
You were timed out from {SERVERNAME} for {TIME} with the reason
```
{REASON}
```\
""")


ROLE_ABOVE = discord.Embed(color=Color.ERROR, title="Permission error", description="""\
The user {USERNAME} has a role above you\
""")

KICK_ERROR_GENERIC = discord.Embed(color=Color.ERROR, title="Error", description="""\
The user {USERNAME} wasn't able to be kicked\
""")

BAN_ERROR_GENERIC = discord.Embed(color=Color.ERROR, title="Error", description="""\
The user {USERNAME} wasn't able to be banned\
""")

TIMEOUT_ERROR_GENERIC = discord.Embed(color=Color.ERROR, title="Error", description="""\
The user {USERNAME} wasn't able to be timed out\
""")


CANNOT_KICK_BOT = discord.Embed(color=Color.ERROR, title="Error", description="""\
I cannot kick bots\
""")

CANNOT_BAN_BOT = discord.Embed(color=Color.ERROR, title="Error", description="""\
I cannot ban bots\
""")

ERROR_CANNOT_TIMEOUT_BOT = discord.Embed(color=Color.ERROR, title="Error", description="""\
I cannot timeout bots\
""")

PURGE = discord.Embed(color=Color.PRIMARY, title="Purged messages", description="""\
Purged {AMOUNT} messages\
""")

PURGE_MAX_AMOUNT = discord.Embed(color=Color.ERROR, title="Error", description="""\
I cannot purge more than 100 messages\
""")


ABOUT = discord.Embed(color=Color.PRIMARY, title=f"About Devoo {Config.VERSION}", description=f"""\
**Devoo** {Config.VERSION} {Config.RELEASE}
Running on Python {version}
Running on Pycord {discord.__version__}\
""")

SITE = discord.Embed(color=Color.PRIMARY, title=f"About Devoo {Config.VERSION}", description=f"""\
You can find more about Devoo here
https://devoopers.net\
""")

SOURCE = discord.Embed(color=Color.PRIMARY, title=f"Devoo {Config.VERSION} Source", description=f"""\
You can find the source code for Devoo here
https://github.com/LmaxplayG/Devoo\
""")

SUPPORT = discord.Embed(color=Color.PRIMARY, title=f"Devoo {Config.VERSION} Support", description=f"""\
You can find the support server for Devoo here
https://discord.gg/54kszbH3bz\
""")


ERROR = discord.Embed(
    color=Color.ERROR, title="An error occured", description="```py\n{ERR}\n```")

RANDOM_ROLL = discord.Embed(
    color=Color.PRIMARY,
    title="Random Roll",
    description="""\
You rolled {NUMBER}\
"""
)

RANDOM_ROLL.set_footer(text="Out of range {MIN} to {MAX}")

RANDOM_MAX_MUST_BE_ABOVE_MIN = discord.Embed(
    color=Color.ERROR,
    title="Min must be above Max",
    description="""\
The parameter `min` MUST be above `max`\
    """
)

RANDOM_COLOR = discord.Embed(
    color=Color.PRIMARY,
    title="Random Color",
    description="""\
Here is your random color: {COLOR}\
""",
)
 