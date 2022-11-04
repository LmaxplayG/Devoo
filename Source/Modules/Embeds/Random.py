import discord as Discord

from Modules.Config import Color

class RandomEmbeds:
    async def random_embed(roll: int, min: int, max: int):
        embed = Discord.Embed(color=Color.PRIMARY, title="Random", description=f"""\
        You rolled a `{roll}`\
        """)
        embed.set_footer(text=f"Min: {min} | Max: {max}")
        return embed