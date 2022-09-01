import discord
from discord.ext import commands
from discord.app_commands import command, describe

from gd.errors import MissingAccess

class Levels(commands.Cog):
	def __init__(self, bot, gd):
		self.bot = bot
		self.gd = gd

	@command(description = "Retrieve information about a level")
	async def levelinfo(self, ctx, id: int):
		try:
			level = await self.gd.get_level(id)
			embed = discord.Embed(colour = discord.Colour.green())
			embed.add_field(name = "Name", value = level.name)
			embed.add_field(name = "Downloads", value = level.downloads)
			embed.add_field(name = "Rating", value = level.rating)
			embed.add_field(
				name = "Stars",
				value = (f"{level.requested_stars} (requested)" if level.stars == 0 else level.stars)
			)
			embed.add_field(name = "Coins", value = level.coins)
			embed.add_field(name = "Creator", value = level.creator.name)
			embed.add_field(name = "Song ID", value = level.song.id)
		except (MissingAccess, AssertionError):
			embed = discord.Embed(colour = discord.Colour.red())
			embed.add_field(name = "Error", value = "That level was not found.")
		finally:
			await ctx.response.send_message(embed = embed)
	
	@command(description = "Check the daily level")
	async def dailylevel(self, ctx):
		level = await self.gd.get_daily()
		embed = discord.Embed(
			colour = discord.Colour.green(),
			title = f"{level.name}: {level.id}",
			description = "Use </levelinfo:1014468288631279696> to view more information about the level"
		)
		await ctx.response.send_message(embed = embed)