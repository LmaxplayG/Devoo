from discord.ext import commands
from .CommandError import on_slash_command_error
from .Message import SetBotForMessageEvent, on_message

def Register(bot: commands.Bot):
    bot.on_application_command_error = on_slash_command_error
    SetBotForMessageEvent(bot)
    bot.event(on_message)