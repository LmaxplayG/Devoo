import datetime
from os import getcwd
import os
from random import random
import sys
import discord
from discord.ext import commands
from discord import ui
import random
import secrets
import copy
import pathlib

from numpy import place


RELEASE = 'Dev'
# RELEASE = 'Release'

VERSION = 'v1.0'

COLOR_PRIMARY = discord.Colour(0x4FEA67)
COLOR_SECONDARY = discord.Colour(0x00BCFF)
#COLOR_WARN      = discord.Colour(0xFF9349)
COLOR_ERROR = discord.Colour(0xFF4D74)

if RELEASE == 'Release':
    LOGO        = discord.File(pathlib.Path(f'{pathlib.Path(__file__).parent.parent.parent}/Assets/Release/web/icon-512-maskable.png'))
    LOGO_MASKED = discord.File(pathlib.Path(f'{pathlib.Path(__file__).parent.parent.parent}/Assets/Release/web/icon-512.png'))
else: 
    LOGO        = discord.File(pathlib.Path(f'{pathlib.Path(__file__).parent.parent.parent}/Assets/Dev/web/icon-512-maskable.png'))
    LOGO_MASKED = discord.File(pathlib.Path(f'{pathlib.Path(__file__).parent.parent.parent}/Assets/Dev/web/icon-512.png'))

# Embeds
EMBED_REQUIRES_PREMIUM = discord.Embed(color=COLOR_ERROR, title="You don't have permission", description="""\
This command requires premium!!!
Buy at https://develoopers.net/premium\
""")

EMBED_REQUIRES_MOD = discord.Embed(color=COLOR_ERROR, title="You don't have permission", description="""\
This requires moderator permissions\
""")


EMBED_MEMBER_KICK = discord.Embed(color=COLOR_PRIMARY, title="Member kicked", description="""\
Kicked {MEMBER} with the reason
```
{REASON}
```\
""")

EMBED_MEMBER_KICK_DM = discord.Embed(color=COLOR_PRIMARY, title="You were kicked from {SERVERNAME}", description="""\
You were kicked from {SERVERNAME} with the reason
```
{REASON}
```\
""")

EMBED_MEMBER_BAN = discord.Embed(color=COLOR_PRIMARY, title="Member kicked", description="""\
Kicked {MEMBER} with the reason
```
{REASON}
```\
""")

EMBED_MEMBER_BAN_DM = discord.Embed(color=COLOR_PRIMARY, title="You were kicked from {SERVERNAME}", description="""\
You were kicked from {SERVERNAME} with the reason
```
{REASON}
```\
""")

EMBED_MEMBER_TIMEOUT = discord.Embed(color=COLOR_PRIMARY, title="Member timed out", description="""\
Timed out {MEMBER} for {TIME} with the reason
```
{REASON}
```\
""")

EMBED_MEMBER_TIMEOUT_DM = discord.Embed(color=COLOR_PRIMARY, title="You were timed out on {SERVERNAME}", description="""\
You were timed out from {SERVERNAME} for {TIME} with the reason
```
{REASON}
```\
""")


EMBED_ROLE_ABOVE = discord.Embed(color=COLOR_ERROR, title="Permission error", description="""\
The user {USERNAME} has a role above you\
""")

EMBED_ERROR_KICK = discord.Embed(color=COLOR_ERROR, title="Error", description="""\
The user {USERNAME} wasn't able to be kicked\
""")

EMBED_ERROR_BAN = discord.Embed(color=COLOR_ERROR, title="Error", description="""\
The user {USERNAME} wasn't able to be banned\
""")

EMBED_ERROR_TIMEOUT = discord.Embed(color=COLOR_ERROR, title="Error", description="""\
The user {USERNAME} wasn't able to be timed out\
""")


EMBED_ERROR_CANNOT_KICK_BOT = discord.Embed(color=COLOR_ERROR, title="Error", description="""\
I cannot kick bots\
""")

EMBED_ERROR_CANNOT_BAN_BOT = discord.Embed(color=COLOR_ERROR, title="Error", description="""\
I cannot ban bots\
""")

EMBED_ERROR_CANNOT_TIMEOUT_BOT = discord.Embed(color=COLOR_ERROR, title="Error", description="""\
I cannot timeout bots\
""")


EMBED_ABOUT = discord.Embed(color=COLOR_PRIMARY, title=f"About Devoo {VERSION}", description=f"""\
**Devoo** {VERSION}
Running on Python {sys.version}
Running on Pycord {discord.__version__}\
""")

EMBED_ERROR = discord.Embed(
    color=COLOR_ERROR, title="An error occured", description="```py\n{ERR}\n```")

EMBED_RANDOM_ROLL = discord.Embed(
    color=COLOR_PRIMARY,
    title="Random Roll",
    description="""\
You rolled {NUMBER}\
"""
)

EMBED_RANDOM_ROLL.set_footer(text="Out of range {MIN} to {MAX}")

EMBED_RANDOM_MAX_MUST_BE_ABOVE_MIN = discord.Embed(
    color=COLOR_ERROR,
    title="Min must be above Max",
    description="""\
The parameter `min` MUST be above `max`\
    """
)

EMBED_RANDOM_COLOR = discord.Embed(
    color=COLOR_PRIMARY,
    title="Random Color",
    description="""\
Here is your random color: {COLOR}\
""",
)
 