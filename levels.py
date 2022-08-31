import discord
from discord.ext import commands
from discord.app_commands import command, describe

class Levels(commands.Cog):
	def __init__(self, bot, gd):
		self.bot = bot
		self.gd = gd

	@command(description = "Retrieve information about a level")
	async def levelinfo(self, ctx, id: int):
		level = await self.gd.get_level(id)

		if level is None:
			embed = discord.Embed(color = discord.Colour.red())
			embed.add_field(name = "Error", value = "That level was not found.")
			await ctx.response.send_message(embed = embed, ephemeral = True)
			return
		
		embed = discord.Embed(color = discord.Colour.green())
		embed.add_field(name = "Name", value = level.name)
		embed.add_field(name = "Description", value = level.description)
		embed.add_field(name = "Downloads", value = level.downloads)
		embed.add_field(name = "Rating", value = level.rating)
		embed.add_field(
			name = "Stars",
			value = (f"{level.requested_stars} (requested)" if level.stars == 0 else level.stars)
		)
		embed.add_field(name = "Coins", value = level.coins)
		embed.add_field(name = "Creator", value = level.creator.name)
		embed.add_field(name = "Song", value = f"[{level.song.name}]({level.song.link})")
		await ctx.response.send_message(embed = embed)