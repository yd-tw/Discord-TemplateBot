import discord
from discord.utils import get

#音樂列表
async def list(ctx):
    await ctx.send("音樂曲目名稱:\n01\n02\n03\n04")

#播放本地音樂
async def play(ctx, file_name, bot, START):
    file_name = "./music/" + file_name + ".mp3"
    voice_channel = get(bot.voice_clients, guild=ctx.guild)
    
    if voice_channel.is_playing():
        await ctx.send(f"音频正在播放，請先使用{START}stop停止")
    else:
        voice_channel.play(discord.FFmpegPCMAudio(file_name))
        await ctx.send(f"正在播放{file_name}")

#停止播放音樂
async def stop(ctx, bot):
    voice_channel = get(bot.voice_clients, guild=ctx.guild)
    
    if voice_channel.is_playing():
        voice_channel.stop()