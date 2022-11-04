import discord              as Discord
import discord.ext.commands as Commands
import copy                 as Copy
import random               as Random
import requests             as Requests

from Modules.Embeds.Fun import EightBallEmbeds, AnimalEmbeds
from Modules.Embeds.Fun import IdenticonEmbeds
from Modules.Embeds.Fun import PingEmbeds



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
        await ctx.respond(embed=EightBallEmbeds.magic8ball(question, responses[Random.randint(0, len(responses) - 1)]))

    @Commands.slash_command(description="Gets the bot's ping")
    async def ping(self, ctx: Discord.ApplicationContext):
        await ctx.defer()
        await ctx.respond(embed=PingEmbeds.ping(ctx.bot.latency * 1000))
# GitHub Copilot generated code with the API links, so don't blame me if it doesn't work

    AnimalGroup = Discord.SlashCommandGroup(description="Gets a random animal", name="animal")

    @AnimalGroup.command(description="Sends a random image of a cat")
    async def cat(self, ctx: Discord.ApplicationContext):
        await ctx.defer()
        url = Requests.get("https://some-random-api.ml/img/cat").json()["link"]
        await ctx.respond(embed=AnimalEmbeds.cat(url))

    @AnimalGroup.command(description="Sends a random image of a dog")
    async def dog(self, ctx: Discord.ApplicationContext):
        await ctx.defer()
        url = Requests.get("https://some-random-api.ml/img/dog").json()["link"]
        await ctx.respond(embed=AnimalEmbeds.dog(url))

    @AnimalGroup.command(description="Sends a random image of a fox")
    async def fox(self, ctx: Discord.ApplicationContext):
        await ctx.defer()
        url = Requests.get("https://some-random-api.ml/img/fox").json()["link"]
        await ctx.respond(embed=AnimalEmbeds.fox(url))

    @AnimalGroup.command(description="Sends a random image of a panda")
    async def panda(self, ctx: Discord.ApplicationContext):
        await ctx.defer()
        url = Requests.get("https://some-random-api.ml/img/panda").json()["link"]
        await ctx.respond(embed=AnimalEmbeds.panda(url))

    @AnimalGroup.command(description="Sends a random image of a red panda")
    async def redpanda(self, ctx: Discord.ApplicationContext):
        await ctx.defer()
        url = Requests.get("https://some-random-api.ml/img/red_panda").json()["link"]
        await ctx.respond(embed=AnimalEmbeds.redPanda(url))

    @AnimalGroup.command(description="Sends a random image of a bird")
    async def bird(self, ctx: Discord.ApplicationContext):
        await ctx.defer()
        url = Requests.get("https://some-random-api.ml/img/birb").json()["link"]
        await ctx.respond(embed=AnimalEmbeds.bird(url))

    @AnimalGroup.command(description="Sends a random image of a koala")
    async def koala(self, ctx: Discord.ApplicationContext):
        await ctx.defer()
        url = Requests.get("https://some-random-api.ml/img/koala").json()["link"]
        await ctx.respond(embed=AnimalEmbeds.koala(url))

    @AnimalGroup.command(description="Sends a random image of a kangaroo")
    async def kangaroo(self, ctx: Discord.ApplicationContext):
        await ctx.defer()
        url = Requests.get("https://some-random-api.ml/img/kangaroo").json()["link"]
        await ctx.respond(embed=AnimalEmbeds.kangaroo(url))

    @AnimalGroup.command(description="Sends a random image of a raccoon")
    async def raccoon(self, ctx: Discord.ApplicationContext):
        await ctx.defer()
        url = Requests.get("https://some-random-api.ml/img/racoon").json()["link"]
        await ctx.respond(embed=AnimalEmbeds.raccoon(url))

    @Commands.slash_command(description="Gets a GitHub users identicon")
    async def identicon(self, ctx: Discord.ApplicationContext, username: str):
        await ctx.defer()

        username = username.replace(" ", "").replace(".", "").replace("-", "")
        
        # We check if https://github.com/identicons/{name}.png exists
        if Requests.get(f"https://github.com/identicons/{username}.png").status_code == 200:
            await ctx.respond(embed=IdenticonEmbeds.identicon(f"https://github.com/identicons/{username}.png", username))
        else:
            await ctx.respond(embed=IdenticonEmbeds.identicon_not_found(username))