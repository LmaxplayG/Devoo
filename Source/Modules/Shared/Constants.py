import discord as Discord
import pathlib as Pathlib
from  .Objects import Release, Version

VERSION = Version(1, 3, 0, Release.DEV)

if VERSION.release == Release.STABLE:
    LOGO        = Discord.File(Pathlib.Path(f'{Pathlib.Path(__file__).parent.parent.parent}/Assets/Release/web/icon-512-maskable.png'))
    LOGO_MASKED = Discord.File(Pathlib.Path(f'{Pathlib.Path(__file__).parent.parent.parent}/Assets/Release/web/icon-512.png'))
else: 
    LOGO        = Discord.File(Pathlib.Path(f'{Pathlib.Path(__file__).parent.parent.parent}/Assets/Dev/web/icon-512-maskable.png'))
    LOGO_MASKED = Discord.File(Pathlib.Path(f'{Pathlib.Path(__file__).parent.parent.parent}/Assets/Dev/web/icon-512.png'))