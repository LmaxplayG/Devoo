import discord as Discord

from Modules.Config import Color

class EightBallEmbeds:
    def magic8ball(question: str, answer: str):
        embed = Discord.Embed(color=Color.PRIMARY, title="Magic 8 Ball", description=f"""\
Question: {question}
Answer: {answer}\
""")
        return embed

class AnimalEmbeds:
    disclaimerText = "I do not own any of these images, they are from https://some-random-api.ml, Devoo is not affiliated with them in any way"

    def cat(link: str):
        embed = Discord.Embed(color=Color.PRIMARY, title="Cat", description="""\
Here is a cat for you\
""")
        embed.set_image(url=link)
        embed.set_footer(text=AnimalEmbeds.disclaimerText)
        return embed

    def dog(link: str):
        embed = Discord.Embed(color=Color.PRIMARY, title="Dog", description="""\
Here is a dog for you\
""")
        embed.set_image(url=link)
        embed.set_footer(text=AnimalEmbeds.disclaimerText)
        return embed

    def bird(link: str):
        embed = Discord.Embed(color=Color.PRIMARY, title="Bird", description="""\
Here is a bird for you\
""")
        embed.set_image(url=link)
        embed.set_footer(text=AnimalEmbeds.disclaimerText)
        return embed

    def fox(link: str):
        embed = Discord.Embed(color=Color.PRIMARY, title="Fox", description="""\
Here is a fox for you\
""")
        embed.set_image(url=link)
        embed.set_footer(text=AnimalEmbeds.disclaimerText)
        return embed

    def redPanda(link: str):
        embed = Discord.Embed(color=Color.PRIMARY, title="Red Panda", description="""\
Here is a red panda for you\
""")
        embed.set_image(url=link)
        embed.set_footer(text=AnimalEmbeds.disclaimerText)
        return embed

    def koala(link: str):
        embed = Discord.Embed(color=Color.PRIMARY, title="Koala", description="""\
Here is a koala for you\
""")
        embed.set_image(url=link)
        embed.set_footer(text=AnimalEmbeds.disclaimerText)
        return embed

    def kangaroo(link: str):
        embed = Discord.Embed(color=Color.PRIMARY, title="Kangaroo", description="""\
Here is a kangaroo for you\
""")
        embed.set_image(url=link)
        embed.set_footer(text=AnimalEmbeds.disclaimerText)
        return embed

    def panda(link: str):
        embed = Discord.Embed(color=Color.PRIMARY, title="Panda", description="""\
Here is a panda for you\
""")
        embed.set_image(url=link)
        embed.set_footer(text=AnimalEmbeds.disclaimerText)
        return embed

    def raccoon(link: str):
        embed = Discord.Embed(color=Color.PRIMARY, title="Raccoon", description="""\
Here is a raccoon for you\
""")
        embed.set_image(url=link)
        embed.set_footer(text=AnimalEmbeds.disclaimer)



class IdenticonEmbeds:
    def identicon(link: str, username: str):
        embed = Discord.Embed(color=Color.PRIMARY, title="Identicon", description=f"""\
Here is the identicon for {username}\
""")
        embed.set_image(url=link)
        return embed

    def identicon_not_found(username: str):
        embed = Discord.Embed(color=Color.PRIMARY, title="Identicon", description="""\
I could not find an identicon for this user.\
""")
        return embed

class PingEmbeds:
    def ping(ping: int):
        ping = round(ping)
        embed = Discord.Embed(color=Color.PRIMARY, title="Ping", description=f"""\
Ping: {ping}ms\
""")
        return embed