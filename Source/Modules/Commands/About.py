import discord              as Discord
import discord.ext.commands as Commands
import copy                 as Copy

from Modules.Embeds.About import AboutEmbeds

class About(Discord.Cog):
    @Commands.slash_command(description="Info about the bot")
    async def about(self, ctx: Discord.ApplicationContext):
        await ctx.defer(ephemeral=True)
        await ctx.respond(embed=AboutEmbeds.about_embed(), ephemeral=True)

    @Commands.slash_command(description="Gives a link to this bots site")
    async def site(self, ctx: Discord.ApplicationContext):
        await ctx.defer(ephemeral=True)
        await ctx.respond(embed=AboutEmbeds.site_embed(), ephemeral=True)

    @Commands.slash_command(description="Gives a link to the TOS")
    async def tos(self, ctx: Discord.ApplicationContext):
        await ctx.defer(ephemeral=True)
        await ctx.respond(embed=AboutEmbeds.tos_embed(), ephemeral=True)

    @Commands.slash_command(description="Gives a link to the privacy policy")
    async def privacy(self, ctx: Discord.ApplicationContext):
        await ctx.defer(ephemeral=True)
        await ctx.respond(embed=AboutEmbeds.privacy_embed(), ephemeral=True)

    @Commands.slash_command(description="Gives a link to this bots source code")
    async def source(self, ctx: Discord.ApplicationContext):
        await ctx.defer(ephemeral=True)
        await ctx.respond(embed=AboutEmbeds.source_embed(), ephemeral=True)

    @Commands.slash_command(description="Gives a link to this bots support server")
    async def support(self, ctx: Discord.ApplicationContext):
        await ctx.defer(ephemeral=True)
        await ctx.respond(embed=AboutEmbeds.support_embed(), ephemeral=True)