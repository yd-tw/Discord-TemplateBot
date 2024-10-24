import discord
from discord.ext import commands
from discord import app_commands
import lib.dataio as dataio

class Money(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(description = "查詢剩餘的金額")
    async def money(
        self, 
        interaction: discord.Interaction,
    ):
        data = dataio.getData(interaction.user.id)
        await interaction.response.send_message(embed=discord.Embed(
            title= data["money"],
            description= "這是你所有的財富",
            color=discord.Colour.random(),
        ))

    @app_commands.command(description = "查詢剩餘的金額")
    async def work(
        self, 
        interaction: discord.Interaction,
    ):
        data = dataio.getData(interaction.user.id)
        dataio.setData(interaction.user.id, {"money": data["money"] + 1})

        await interaction.response.send_message(embed=discord.Embed(
            title= "工作完成",
            description= f"@{interaction.user.id}有空歡迎再次前來工作!",
            color=discord.Colour.random(),
        ))

async def setup(bot: commands.Bot):
    await bot.add_cog(Money(bot))