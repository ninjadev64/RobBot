import discord
from discord.ext import commands
from discord.app_commands import command, describe

class Songs(commands.Cog):
	def __init__(self, bot, gd):
		self.bot = bot
		self.gd = gd
	
	@command(description = "Retrieve information about a song on Newgrounds")
	async def songinfo(self, ctx, id: int):
		song = await self.gd.get_song(id)

		if song is None:
			embed = discord.Embed(color = discord.Colour.red())
			embed.add_field(name = "Error", value = "That song was not found.")
			await ctx.response.send_message(embed = embed, ephemeral = True)
			return
		
		embed = discord.Embed(color = discord.Colour.green())
		embed.title = f"{song.name} by {song.author}"
		embed.description = song.link

		await ctx.response.send_message(embed = embed)