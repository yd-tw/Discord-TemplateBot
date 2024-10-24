import discord
from discord.ext import commands
from discord import app_commands
import random

class Game(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(description = "貓咪幫你預測事情發生的機率")
    async def percent(
        self, 
        interaction: discord.Interaction,
        text: str,
    ):
        probability = random.uniform(0,100)
        await interaction.response.send_message(embed=discord.Embed(
            title= text,
            description=f"機率為: {probability:.2f}%",
            color=discord.Colour.random(),
        ))
    
    @app_commands.command(description = "貓咪投骰子")
    async def dice(
        self, 
        interaction: discord.Interaction,
    ):
        probability = random.choices([1,2,3,4,5,6])
        await interaction.response.send_message(embed=discord.Embed(
            title= probability,
            description= "需要重新一次嗎...?",
            color=discord.Colour.random(),
        ))

async def setup(bot: commands.Bot):
    await bot.add_cog(Game(bot))