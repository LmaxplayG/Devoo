"""
Configuration
"""

from random import random
import discord
import pathlib

from numpy import place

RELEASE = 'Dev'
# RELEASE = 'Release'

VERSION = 'v1.0.2'

if RELEASE == 'Release':
    LOGO        = discord.File(pathlib.Path(f'{pathlib.Path(__file__).parent.parent.parent}/Assets/Release/web/icon-512-maskable.png'))
    LOGO_MASKED = discord.File(pathlib.Path(f'{pathlib.Path(__file__).parent.parent.parent}/Assets/Release/web/icon-512.png'))
else: 
    LOGO        = discord.File(pathlib.Path(f'{pathlib.Path(__file__).parent.parent.parent}/Assets/Dev/web/icon-512-maskable.png'))
    LOGO_MASKED = discord.File(pathlib.Path(f'{pathlib.Path(__file__).parent.parent.parent}/Assets/Dev/web/icon-512.png'))
