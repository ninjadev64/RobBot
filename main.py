import discord
from discord.ext.commands import Bot as dBot

from levels import Levels
from users import Users
from songs import Songs

from os import environ, system
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv(dotenv_path = "tokens.env")

import gd
client = gd.Client()

class Bot(dBot):
	async def setup_hook(self):
		await self.add_cog(Levels(self, client))
		await self.add_cog(Users(self, client))
		await self.add_cog(Songs(self, client))
		await self.tree.sync()
		self.remove_command("help")

intents = discord.Intents.default()
intents.message_content = True
bot = Bot(command_prefix = "?", intents = intents)

@bot.event
async def on_ready():
	for guild in bot.guilds: print(guild.name)
	await bot.change_presence(activity = discord.Streaming(
		name = "Geometry Dash",
		url = "https://www.youtube.com/watch?v=xvFZjo5PgG0"
	))

keep_alive()

try: bot.run(environ["TOKEN"]) 
except discord.errors.HTTPException: system("kill 1")