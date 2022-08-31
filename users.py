import discord
from discord.ext import commands
from discord.app_commands import command, describe

class Users(commands.Cog):
	def __init__(self, bot, gd):
		self.bot = bot
		self.gd = gd
	
	@command(description = "Get info about a user")
	async def userinfo(self, ctx, id: int):
		user = await (await self.gd.get_user(id)).to_user()

		embed = discord.Embed(color = discord.Colour.green())
		embed.add_field(name = "Name", value = user.name)
		embed.add_field(name = "Secret Coins", value = user.coins)
		embed.add_field(name = "User Coins", value = user.user_coins)
		embed.add_field(name = "Demons", value = user.demons)
		embed.add_field(name = "Diamonds", value = user.diamonds)

		await ctx.response.send_message(embed = embed)
		
	@command(description = "Get a user's ID from their name")
	async def userid(self, ctx, name: str):
		user = await self.gd.find_user(name)

		if user is None:
			embed = discord.Embed(color = discord.Colour.red())
			embed.add_field(name = "Error", value = "That user was not found.")
			await ctx.response.send_message(embed = embed, ephemeral = True)
			return
		
		embed = discord.Embed(color = discord.Colour.green(), title = f"{name}'s User ID", description = user.account_id)
		await ctx.response.send_message(embed = embed)