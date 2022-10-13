import discord
from discord.ext import commands
import copy
from Modules.Config import Embed
import secrets

class Random(commands.Cog):
    @commands.slash_command(description="Gets a random number", name="random")
    async def random_(self, ctx: discord.ApplicationContext, min: int = 0, max: int = 100):
        await ctx.defer()
        if(max <= min):
            await ctx.respond(embed=Embed.RANDOM_MAX_MUST_BE_ABOVE_MIN)
        roll = (secrets.randbelow(max - min) + min)
        embed = copy.deepcopy(Embed.RANDOM_ROLL)
        embed.description = embed.description.replace("{NUMBER}", roll.__str__())
        embed.set_footer(text=embed.footer.text.replace('{MIN}', min.__str__()).replace('{MAX}', max.__str__()))

        await ctx.respond(embed=embed)

    @commands.slash_command(description="Gets a random color", name="random-color")
    async def randomcolor(self, ctx: discord.ApplicationContext):
        await ctx.defer()
        roll = secrets.randbelow(0x1000000)
        embed = copy.deepcopy(Embed.RANDOM_COLOR)
        embed.color = discord.Colour(value=roll)
        embed.description = embed.description.replace("{COLOR}", hex(roll).upper().replace('0X', '#'))

        await ctx.respond(embed=embed)

    @commands.slash_command(description="Gets a random member", name="random-member")
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def randommember(self, ctx: discord.ApplicationContext):
        await ctx.defer()
        roll = secrets.choice(ctx.guild.members)
        embed = copy.deepcopy(Embed.RANDOM_MEMBER)
        embed.description = embed.description.replace("{MEMBER}", roll.mention)

        await ctx.respond(embed=embed)