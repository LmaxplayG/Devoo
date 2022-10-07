"""
Configuration
"""

import datetime
from os import getcwd
import os
from random import random
import sys
import discord
from discord.ext import commands
from discord import ui
import random
import secrets
import copy
import pathlib

from numpy import place

RELEASE = 'Dev'
# RELEASE = 'Release'

VERSION = 'v1.0.1'

if RELEASE == 'Release':
    LOGO        = discord.File(pathlib.Path(f'{pathlib.Path(__file__).parent.parent.parent}/Assets/Release/web/icon-512-maskable.png'))
    LOGO_MASKED = discord.File(pathlib.Path(f'{pathlib.Path(__file__).parent.parent.parent}/Assets/Release/web/icon-512.png'))
else: 
    LOGO        = discord.File(pathlib.Path(f'{pathlib.Path(__file__).parent.parent.parent}/Assets/Dev/web/icon-512-maskable.png'))
    LOGO_MASKED = discord.File(pathlib.Path(f'{pathlib.Path(__file__).parent.parent.parent}/Assets/Dev/web/icon-512.png'))
