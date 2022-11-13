import discord as Discord

from Modules.Config import Color

class RandomEmbeds:
    async def random_embed(roll: int, min: int, max: int):
        embed = Discord.Embed(color=Color.PRIMARY, title="Random", description=f"""\
        You rolled a `{roll}`\
        """)
        embed.set_footer(text=f"Min: {min} | Max: {max}")
        return embed
    
    async def max_must_be_greater_than_min_embed():
        embed = Discord.Embed(color=Color.ERROR, title="Error", description=f"""\
        Max must be greater than min\
        """)
        return embed
    
    async def random_color_embed(color: int):
        embed = Discord.Embed(color=color, title="Random Color", description=f"""\
        You rolled a `{hex(color).upper().replace('0X', '#')}`\
        """)
        return embed