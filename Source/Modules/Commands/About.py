import discord              as Discord
import discord.ext.commands as Commands
import copy                 as Copy
import Modules.Config.Embed as Embed

class About(Discord.Cog):
    @Commands.slash_command(description="Info about the bot")
    async def about(self, ctx: Discord.ApplicationContext):
        embed = Copy.deepcopy(Embed.ABOUT)
        await ctx.respond(embed=embed, ephemeral=True)

    @Commands.slash_command(description="Gives a link to this bots site")
    async def site(self, ctx: Discord.ApplicationContext):
        embed = Copy.deepcopy(Embed.SITE)
        await ctx.respond(embed=embed, ephemeral=True)
    
    @Commands.slash_command(description="Gives a link to this bots source code")
    async def source(self, ctx: Discord.ApplicationContext):
        embed = Copy.deepcopy(Embed.SOURCE)
        await ctx.respond(embed=embed, ephemeral=True)

    @Commands.slash_command(description="Gives a link to this bots support server")
    async def support(self, ctx: Discord.ApplicationContext):
        embed = Copy.deepcopy(Embed.SUPPORT)
        await ctx.respond(embed=embed, ephemeral=True)
