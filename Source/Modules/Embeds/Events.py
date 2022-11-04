import discord as Discord

from Modules.Config import Color


class SlashCommandErrorEmbeds:
    def __init__(self):
        pass

    def slash_command_error_embed(error: Exception):
        embed = Discord.Embed(
            title="Slash Command Error",
            description=f"""\
            An error occured while processing your slash command. Please try again later.
            Error: `{error.with_traceback(None)}`""",
            color=Color.ERROR
        )
        return embed
    
    def no_private_message():
        embed = Discord.Embed(
            title="Slash Command Error",
            description="""This slash commands can only be used in servers.""",
            color=Color.ERROR
        )
        return embed

    def missing_permissions_embed(missing_permissions: list[str]):
        embed = Discord.Embed(
            title="Slash Command Error",
            description="""You are missing the following permissions: `{PERMISSIONS}`""",
            color=Color.ERROR
        )
        embed.description = embed.description.replace(
            "{PERMISSIONS}", ", ".join(missing_permissions))
        return embed

    def missing_permissions_embed_bot(missing_permissions: list[str]):
        embed = Discord.Embed(
            title="Slash Command Error",
            description="""I am missing the following permissions: `{PERMISSIONS}`""",
            color=Color.ERROR
        )
        embed.description = embed.description.replace(
            "{PERMISSIONS}", ", ".join(missing_permissions))
        return embed