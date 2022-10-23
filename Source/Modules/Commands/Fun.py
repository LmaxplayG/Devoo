import discord              as Discord
import discord.ext.commands as Commands
import copy                 as Copy
import random               as Random
import requests             as Requests

import Modules.Config.Embed as Embed


class Fun(Commands.Cog):
    @Commands.slash_command(description="Magic 8 Ball", name="8-ball")
    async def magic8ball(self, ctx: Discord.ApplicationContext, question: str):
        await ctx.defer()
        responses = ['It is certain.',
                     'It is decidedly so.',
                     'Without a doubt.',
                     'Yes - definitely.',
                     'You may rely on it.',
                     'As I see it, yes.',
                     'Most likely.',
                     'Outlook good.',
                     'Yes.',
                     'Signs point to yes.',
                     'Reply hazy, try again.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     "Don't count on it.",
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Very doubtful.']
        embed = Copy.deepcopy(Embed.MAGIC8BALL)
        embed.description = embed.description.replace(
            '{QUESTION}', question).replace('{ANSWER}', Random.choice(responses))
        embed.title = embed.title.replace(
            '{USERNAME}', ctx.author.name).replace("{QUESTION}", question)
        await ctx.respond(embed=embed, ephemeral=True)

    @Commands.slash_command(description="Calculates the time difference between two users")
    async def ping(self, ctx: Discord.ApplicationContext, user1: Discord.Member, user2: Discord.Member = None):
        await ctx.defer()
        if user2 == None:
            user2 = ctx.author
        embed = Copy.deepcopy(Embed.PING)
        embed.description = embed.description.replace('{USER1}', user1.mention).replace(
            '{USER2}', user2.mention).replace('{PING}', str(abs(user1.created_at - user2.created_at)))
        await ctx.respond(embed=embed, ephemeral=True)

# GitHub Copilot generated code with the API links, so don't blame me if it doesn't work

    @Commands.slash_command(description="Sends a random image of a cat")
    async def cat(self, ctx: Discord.ApplicationContext):
        await ctx.defer()
        embed = Copy.deepcopy(Embed.CAT)
        embed.set_image(url=Requests.get(
            "https://some-random-api.ml/img/cat").json()["link"])
        await ctx.respond(embed=embed, ephemeral=True)

    @Commands.slash_command(description="Sends a random image of a dog")
    async def dog(self, ctx: Discord.ApplicationContext):
        await ctx.defer()
        embed = Copy.deepcopy(Embed.DOG)
        embed.set_image(url=Requests.get(
            "https://some-random-api.ml/img/dog").json()["link"])
        await ctx.respond(embed=embed)

    @Commands.slash_command(description="Sends a random image of a bird")
    async def bird(self, ctx: Discord.ApplicationContext):
        await ctx.defer()
        embed = Copy.deepcopy(Embed.BIRD)

        embed.set_image(url=Requests.get(
            "https://some-random-api.ml/img/birb").json()["link"])
        await ctx.respond(embed=embed)

    @Commands.slash_command(description="Sends a random image of a fox")
    async def fox(self, ctx: Discord.ApplicationContext):
        await ctx.defer()
        embed = Copy.deepcopy(Embed.FOX)

        embed.set_image(url=Requests.get(
            "https://some-random-api.ml/img/fox").json()["link"])
        await ctx.respond(embed=embed)

    @Commands.slash_command(description="Sends a random image of a panda")
    async def panda(self, ctx: Discord.ApplicationContext):
        await ctx.defer()
        embed = Copy.deepcopy(Embed.PANDA)

        embed.set_image(url=Requests.get(
            "https://some-random-api.ml/img/panda").json()["link"])
        await ctx.respond(embed=embed)

    @Commands.slash_command(description="Sends a random image of a red panda")
    async def redpanda(self, ctx: Discord.ApplicationContext):
        await ctx.defer()
        embed = Copy.deepcopy(Embed.REDPANDA)

        embed.set_image(url=Requests.get(
            "https://some-random-api.ml/img/red_panda").json()["link"])
        await ctx.respond(embed=embed)

    @Commands.slash_command(description="Sends a random image of a koala")
    async def koala(self, ctx: Discord.ApplicationContext):
        await ctx.defer()
        embed = Copy.deepcopy(Embed.KOALA)

        embed.set_image(url=Requests.get(
            "https://some-random-api.ml/img/koala").json()["link"])
        await ctx.respond(embed=embed)

    @Commands.slash_command(description="Sends a random image of a kangaroo")
    async def kangaroo(self, ctx: Discord.ApplicationContext):
        await ctx.defer()
        embed = Copy.deepcopy(Embed.KANGAROO)

        embed.set_image(url=Requests.get(
            "https://some-random-api.ml/img/kangaroo").json()["link"])
        await ctx.respond(embed=embed)

    @Commands.slash_command(description="Sends a random image of a raccoon")
    async def raccoon(self, ctx: Discord.ApplicationContext):
        await ctx.defer()
        embed = Copy.deepcopy(Embed.RACCOON)

        embed.set_image(url=Requests.get(
            "https://some-random-api.ml/img/racoon").json()["link"])
        await ctx.respond(embed=embed)

    @Commands.slash_command(description="Gets a GitHub users identicon")
    async def identicon(self, ctx: Discord.ApplicationContext, username: str):
        await ctx.defer()
        # We check if https://github.com/identicons/{name}.png exists
        if Requests.get(f"https://github.com/identicons/{username}.png").status_code == 200:
            embed = Copy.deepcopy(Embed.IDENTICON)
            embed.set_image(url=f"https://github.com/identicons/{username}.png")
            embed.set_footer(text=embed.footer.text.replace(
                '{USERNAME}', username))
            await ctx.respond(embed=embed)
        else:
            embed = Copy.deepcopy(Embed.IDENTICON_NOT_FOUND)
            embed.description = embed.description.replace(
                '{USERNAME}', username)
            await ctx.respond(embed=embed)