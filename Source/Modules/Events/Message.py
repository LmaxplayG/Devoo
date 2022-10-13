import discord

bot: discord.Bot

def SetBotForMessageEvent(_bot: discord.Bot):
    global bot
    bot = _bot

async def on_message(message: discord.Message):
    if message.author == bot.user:
        return