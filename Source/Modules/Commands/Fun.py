import datetime
import discord
from discord.ext import commands
import copy
import random

import requests
from Modules.Config import Embed
from Modules.Shared import RequireMod

class Fun(commands.Cog):
    @commands.slash_command(description="Magic 8 Ball", name="8-ball")
    async def magic8ball(self, ctx: discord.ApplicationContext, question: str):
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
        embed = copy.deepcopy(Embed.MAGIC8BALL)
        embed.description = embed.description.replace('{QUESTION}', question).replace('{ANSWER}', random.choice(responses))
        embed.title = embed.title.replace('{USERNAME}', ctx.author.name).replace("{QUESTION}", question)
        await ctx.respond(embed=embed, ephemeral=True)

    @commands.slash_command(description="Calculates the time difference between two users")
    async def ping(self, ctx: discord.ApplicationContext, user1: discord.Member, user2: discord.Member = None):
        await ctx.defer()
        if user2 == None:
            user2 = ctx.author
        embed = copy.deepcopy(Embed.PING)
        embed.description = embed.description.replace('{USER1}', user1.mention).replace('{USER2}', user2.mention).replace('{PING}', str(abs(user1.created_at - user2.created_at)))
        await ctx.respond(embed=embed, ephemeral=True)

# GitHub Copilot generated code with the API links, so don't blame me if it doesn't work

    @commands.slash_command(description="Sends a random image of a cat")
    async def cat(self, ctx: discord.ApplicationContext):
        await ctx.defer()
        embed = copy.deepcopy(Embed.CAT)
        embed.set_image(url=requests.get("https://some-random-api.ml/img/cat").json()["link"])
        await ctx.respond(embed=embed, ephemeral=True)

    @commands.slash_command(description="Sends a random image of a dog")
    async def dog(self, ctx: discord.ApplicationContext):
        await ctx.defer()
        embed = copy.deepcopy(Embed.DOG)
        embed.set_image(url=requests.get("https://some-random-api.ml/img/dog").json()["link"])
        await ctx.respond(embed=embed)

    @commands.slash_command(description="Sends a random image of a bird")
    async def bird(self, ctx: discord.ApplicationContext):
        await ctx.defer()
        embed = copy.deepcopy(Embed.BIRD)
        # Request to https://some-random-api.ml/img/birb
        # Returns a JSON object with a key "link" which contains the URL to the image
        embed.set_image(url=requests.get("https://some-random-api.ml/img/birb").json()["link"])
        await ctx.respond(embed=embed)

    @commands.slash_command(description="Sends a random image of a fox")
    async def fox(self, ctx: discord.ApplicationContext):
        await ctx.defer()
        embed = copy.deepcopy(Embed.FOX)

        embed.set_image(url=requests.get("https://some-random-api.ml/img/fox").json()["link"])
        await ctx.respond(embed=embed)