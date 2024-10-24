import discord
from discord.ext import commands
from discord import app_commands

class Event(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(
        self, 
        message: discord.Message
    ):
        if message.author == self.bot.user:
            return
        if message.content == "早安":
            await message.channel.send("早安")
        if message.content == "午安":
            await message.channel.send("午安")
        if message.content == "晚安":
            await message.channel.send("晚安")

async def setup(bot: commands.Bot):
    await bot.add_cog(Event(bot))