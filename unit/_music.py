import os
import discord
from discord.utils import get

#音樂列表
async def list(ctx):
    fileList = os.listdir("./data/music/")
    sendList = "音樂曲目列表:\n"
    for name in fileList:
        sendList = sendList + name[:-4] + "\n"
    await ctx.respond(sendList)

#播放本地音樂
async def play(ctx, file, bot, MUSICPATH):
    voice_channel = get(bot.voice_clients, guild=ctx.guild)
    
    if voice_channel.is_playing():
        await ctx.respond(f"音频正在播放，請先使用/stop停止")
    else:
        voice_channel.play(discord.FFmpegPCMAudio("./" + MUSICPATH + file + ".mp3"))
        await ctx.respond(f"正在播放{file}")

#停止播放音樂
async def stop(ctx, bot):
    voice_channel = get(bot.voice_clients, guild=ctx.guild)
    
    if voice_channel.is_playing():
        voice_channel.stop()