import datetime
import discord
from discord.ext import commands
import copy
from Modules.Config import Config, Embed
from Modules.Shared import RequireMod
import secrets

class Random(commands.Cog):
    @commands.slash_command(description="Gets a random number", name="random")
    async def random_(self, ctx: discord.ApplicationContext, min: int = 0, max: int = 100):
        if(max <= min):
            await ctx.respond(embed=Embed.RANDOM_MAX_MUST_BE_ABOVE_MIN)
        roll = (secrets.randbelow(max - min) + min)
        embed = copy.copy(Embed.RANDOM_ROLL)
        embed.description = embed.description.replace("{NUMBER}", roll.__str__())
        embed.set_footer(text=embed.footer.text.replace('{MIN}', min.__str__()).replace('{MAX}', max.__str__()))

        await ctx.respond(embed=embed)

    @commands.slash_command(description="Gets a random color", name="random-color")
    async def randomcolor(self, ctx: discord.ApplicationContext):
        roll = secrets.randbelow(0x1000000)
        embed = copy.copy(Embed.RANDOM_COLOR)
        embed.color = discord.Colour(value=roll)
        embed.description = embed.description.replace("{COLOR}", hex(roll).upper().replace('0X', '#'))

        await ctx.respond(embed=embed)
