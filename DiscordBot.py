import os
from discord import Intents
from discord_easy_commands import EasyBot

intents = Intents.default()

bot = EasyBot(intents=intents)
members = bot.get_members()
bot.setCommand("!Ping", "Pong!")

bot.run(os.environ["TOKEN"])