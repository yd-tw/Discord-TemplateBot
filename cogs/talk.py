import discord
from discord.ext import commands
from discord import app_commands
import asyncio

class Main(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(description = "讓貓咪幫你說一段話數次")
    async def say(
        self, 
        interaction: discord.Interaction,
        text: str,
        times: int,
    ):
        if times > 50:
            await interaction.response.send_message(embed=discord.Embed(
                description= "到底是誰同意你輸入這麼大的數字?",
                color= discord.Colour.random(),
            ))
        else:
            await interaction.response.send_message(embed=discord.Embed(
                description= "訊息已受理",
                color= discord.Colour.random(),
            ))
            for _ in range(times):
                await interaction.followup.send(embed=discord.Embed(
                    description= text,
                    color= discord.Colour.random(),
                ))
                await asyncio.sleep(1)

    @app_commands.command(description = "查詢程式貓版本")
    async def version(
        self, 
        interaction: discord.Interaction, 
    ):
        await interaction.response.send_message(embed=discord.Embed(
            description= f"當前版本: 1.4.0",
            color= discord.Colour.random(),
        ))

    @app_commands.command(description = "查詢程式貓邀請連結")
    async def invite(
        self, 
        interaction: discord.Interaction,
    ):
        await interaction.response.send_message(embed=discord.Embed(
            description= "邀我到其他伺服器!!!\nhttps://discord.com/oauth2/authorize?client_id=1145187780364869651&permissions=0&scope=bot",
            color= discord.Colour.random(),
        ))

    @app_commands.command(description = "查詢程式貓延遲")
    async def ping(
        self, 
        interaction: discord.Interaction, 
    ):
        latency = self.bot.latency * 1000  # 將延遲轉換為毫秒
        await interaction.response.send_message(embed=discord.Embed(
            description= f'機器人延遲為 {latency:.2f} 毫秒',
            color= discord.Colour.random(),
        ))

async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot))