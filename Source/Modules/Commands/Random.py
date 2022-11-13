import discord as Discord
import discord.ext.commands as Commands
import copy as Copy
import secrets


from Modules.Embeds.Random import RandomEmbeds


class Random(Commands.Cog):
    @Commands.slash_command(description="Gets a random number", name="random")
    async def random_(self, ctx: Discord.ApplicationContext, min: int = 0, max: int = 100):
        await ctx.defer()
        if(max <= min):
            await ctx.respond(embed=await RandomEmbeds.max_must_be_greater_than_min_embed())
        roll = (secrets.randbelow(max - min) + min)

        await ctx.respond(embed=await RandomEmbeds.random_embed(roll, min, max))

    @Commands.slash_command(description="Gets a random color", name="random-color")
    async def randomcolor(self, ctx: Discord.ApplicationContext):
        await ctx.defer()
        roll = secrets.randbelow(0x1000000)
        await ctx.respond(embed=RandomEmbeds.random_color_embed(roll))

    # @Commands.slash_command(description="Gets a random member", name="random-member")
    # @Commands.guild_only()
    # @Commands.has_permissions(kick_members=True)
    # async def randommember(self, ctx: Discord.ApplicationContext):
        # await ctx.defer()
        # roll = secrets.choice(ctx.guild.members)
        # embed = Copy.deepcopy(Embed.RANDOM_MEMBER)
        # embed.description = embed.description.replace("{MEMBER}", roll.mention)
# 
        # await ctx.respond(embed=embed)