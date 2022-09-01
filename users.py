import discord
from discord.ext import commands
from discord.app_commands import command, describe

from gd.errors import MissingAccess

class Users(commands.Cog):
	def __init__(self, bot, gd):
		self.bot = bot
		self.gd = gd
	
	@command(description = "Get info about a user")
	async def userinfo(self, ctx, id: int):
		try:
			user = await (await self.gd.get_user(id)).to_user()
			embed = discord.Embed(colour = discord.Colour.green())
			embed.add_field(name = "Name", value = user.name)
			embed.add_field(name = "Secret Coins", value = user.coins)
			embed.add_field(name = "User Coins", value = user.user_coins)
			embed.add_field(name = "Demons", value = user.demons)
			embed.add_field(name = "Diamonds", value = user.diamonds)
		except (MissingAccess, AssertionError):
			embed = discord.Embed(colour = discord.Colour.red())
			embed.add_field(name = "Error", value = "That user was not found.")
		finally:
			await ctx.response.send_message(embed = embed)
		
	@command(description = "Get a user's ID from their name")
	async def userid(self, ctx, name: str):
		try:
			user = await self.gd.find_user(name)
			embed = discord.Embed(colour = discord.Colour.green(), title = f"{name}'s User ID", description = user.account_id)
		except (MissingAccess, AssertionError):
			embed = discord.Embed(colour = discord.Colour.red())
			embed.add_field(name = "Error", value = "That user was not found.")
		finally:
			await ctx.response.send_message(embed = embed)