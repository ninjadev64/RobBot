import discord
from discord.ext import commands
from discord.app_commands import command, describe

from gd.errors import MissingAccess

class Songs(commands.Cog):
	def __init__(self, bot, gd):
		self.bot = bot
		self.gd = gd
	
	@command(description = "Retrieve information about a song on Newgrounds")
	async def songinfo(self, ctx, id: int):
		try:
			song = await self.gd.get_song(id)
			embed = discord.Embed(color = discord.Colour.green())
			embed.title = f"{song.name} by {song.author}"
			embed.description = song.link
		except (MissingAccess, AssertionError):
			embed = discord.Embed(color = discord.Colour.red())
			embed.add_field(name = "Error", value = "That song was not found.")
		finally:
			await ctx.response.send_message(embed = embed)