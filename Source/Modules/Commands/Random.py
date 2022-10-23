import discord as Discord
import discord.ext.commands as Commands
import copy as Copy
import Modules.Config.Embed as Embed
import secrets

class Random(Commands.Cog):
    @Commands.slash_command(description="Gets a random number", name="random")
    async def random_(self, ctx: Discord.ApplicationContext, min: int = 0, max: int = 100):
        await ctx.defer()
        if(max <= min):
            await ctx.respond(embed=Embed.RANDOM_MAX_MUST_BE_ABOVE_MIN)
        roll = (secrets.randbelow(max - min) + min)
        embed = Copy.deepcopy(Embed.RANDOM_ROLL)
        embed.description = embed.description.replace("{NUMBER}", roll.__str__())
        embed.set_footer(text=embed.footer.text.replace('{MIN}', min.__str__()).replace('{MAX}', max.__str__()))

        await ctx.respond(embed=embed)

    @Commands.slash_command(description="Gets a random color", name="random-color")
    async def randomcolor(self, ctx: Discord.ApplicationContext):
        await ctx.defer()
        roll = secrets.randbelow(0x1000000)
        embed = Copy.deepcopy(Embed.RANDOM_COLOR)
        embed.color = Discord.Colour(value=roll)
        embed.description = embed.description.replace("{COLOR}", hex(roll).upper().replace('0X', '#'))

        await ctx.respond(embed=embed)

    @Commands.slash_command(description="Gets a random member", name="random-member")
    @Commands.guild_only()
    @Commands.has_permissions(kick_members=True)
    async def randommember(self, ctx: Discord.ApplicationContext):
        await ctx.defer()
        roll = secrets.choice(ctx.guild.members)
        embed = Copy.deepcopy(Embed.RANDOM_MEMBER)
        embed.description = embed.description.replace("{MEMBER}", roll.mention)

        await ctx.respond(embed=embed)