
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

MEMBER_MUTE = discord.Embed(color=Color.PRIMARY, title="Member muted", description="""\
Muted {MEMBER} with the reason
```
{REASON}
```\
""")

MEMBER_MUTE_DM = discord.Embed(color=Color.PRIMARY, title="You were muted on {SERVERNAME}", description="""\
You were muted on {SERVERNAME} with the reason
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

MAGIC8BALL = discord.Embed(color=Color.PRIMARY, title="Magic 8 Ball", description="""\
Question: {QUESTION}
Answer: {ANSWER}\
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


NO_DM = discord.Embed(color=Color.ERROR, title="Error", description="""\
This command cannot be used in DMs\
""")

DISCLAIMER_ANIMAL_PICS = "I do not own any of these images, they are from https://some-random-api.ml, Devoo is not affiliated with them in any way"

CAT = discord.Embed(color=Color.PRIMARY, title="Cat", description="""\
Here is a cat for you\
""")

CAT.set_footer(text=DISCLAIMER_ANIMAL_PICS)

DOG = discord.Embed(color=Color.PRIMARY, title="Dog", description="""\
Here is a dog for you\
""")

DOG.set_footer(text=DISCLAIMER_ANIMAL_PICS)

BIRD = discord.Embed(color=Color.PRIMARY, title="Bird", description="""\
Here is a bird for you\
""")

BIRD.set_footer(text=DISCLAIMER_ANIMAL_PICS)

FOX = discord.Embed(color=Color.PRIMARY, title="Fox", description="""\
Here is a fox for you\
""")

FOX.set_footer(text=DISCLAIMER_ANIMAL_PICS)

REDPANDA = discord.Embed(color=Color.PRIMARY, title="Red Panda", description="""\
Here is a red panda for you\
""")

REDPANDA.set_footer(text=DISCLAIMER_ANIMAL_PICS)

KOALA = discord.Embed(color=Color.PRIMARY, title="Koala", description="""\
Here is a koala for you\
""")

KOALA.set_footer(text=DISCLAIMER_ANIMAL_PICS)

KANGAROO = discord.Embed(color=Color.PRIMARY, title="Kangaroo", description="""\
Here is a kangaroo for you\
""")

KANGAROO.set_footer(text=DISCLAIMER_ANIMAL_PICS)

PANDA = discord.Embed(color=Color.PRIMARY, title="Panda", description="""\
Here is a panda for you\
""")

PANDA.set_footer(text=DISCLAIMER_ANIMAL_PICS)

RACCOON = discord.Embed(color=Color.PRIMARY, title="Raccoon", description="""\
Here is a raccoon for you\
""")

RACCOON.set_footer(text=DISCLAIMER_ANIMAL_PICS)

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
