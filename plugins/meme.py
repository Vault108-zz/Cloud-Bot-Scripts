import os
import codecs
import random
import asyncio

from cloudbot import hook


@hook.on_start()
def load_meme(bot):
    path = os.path.join(bot.vault_dir, "meme.txt")
    global meme
    with codecs.open(path, encoding="utf-8") as f:
        meme = [line.strip() for line in f.readlines() if not line.startswith("//")]


@asyncio.coroutine
@hook.command(autohelp=False)
def meme():
    """MEME"""
    return random.choice(meme)
