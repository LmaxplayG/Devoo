import discord as Discord
import pathlib as Pathlib
import os      as OS
import sys     as Sys

from Modules.Config import Color

from Modules.Shared.Objects import Release, Version
from Modules.Shared import Constants

class AboutEmbeds:
    """
    Embeds for /about
    """
    def about_embed():
        embed = Discord.Embed(color=Color.PRIMARY, title="About", description=f"""\
        **Devoo** {Constants.VERSION}
        Python: {Sys.version.split(' ')[0]}
        PyCord: {Discord.__version__}
        """)
        return embed

    def site_embed():
        embed = Discord.Embed(color=Color.PRIMARY, title="Devoo", description=f"""\
        You can find more information about Devoo on our website!
        [Click here to visit](https://devoopers.net/)
        """)
        return embed
    
    def tos_embed():
        embed = Discord.Embed(color=Color.PRIMARY, title="Terms of Service", description=f"""\
        You can find our Terms of Service [here](https://devoopers.net/legal-stuff/terms)
        Please remember to follow [Discord's Terms of Service](https://discord.com/terms) when using Devoo.
        """)
        return embed

    def privacy_embed():
        embed = Discord.Embed(color=Color.PRIMARY, title="Privacy Policy", description=f"""\
        You can find our Privacy Policy [here](https://devoopers.net/legal-stuff/privacy)
        The privacy policy for Discord can be found [here](https://discord.com/privacy)
        """)
        return embed

    def source_embed():
        embed = Discord.Embed(color=Color.PRIMARY, title="Source Code", description=f"""\
        You can find the source code for Devoo [here](https://github.com/LmaxplayG/Devoo)
        """)
        return embed

    def support_embed():
        embed = Discord.Embed(color=Color.PRIMARY, title="Support Server", description=f"""\
        You can join our support server [here](https://discord.gg/54kszbH3bz)
        """)
        return embed