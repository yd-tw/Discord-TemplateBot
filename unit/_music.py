import os
import discord
from discord.utils import get

#音樂列表
async def musicfile(ctx):
    fileList = os.listdir("./data/music/")
    sendList = "音樂曲目列表:\n"
    for name in fileList:
        sendList = sendList + name[:-4] + "\n"
    await ctx.respond(embed=discord.Embed(
        description= sendList,
        color= discord.Colour.random(),
    ))

#播放本地音樂
async def musicplay(ctx, file, bot, MUSICPATH):
    voice_channel = get(bot.voice_clients, guild=ctx.guild)
    
    if voice_channel.is_playing():
        voice_channel.stop()
    
    voice_channel.play(discord.FFmpegPCMAudio("./" + MUSICPATH + file + ".mp3"))
    await ctx.respond(embed=discord.Embed(
        description= f"正在播放{file}",
        color= discord.Colour.random(),
    ))

#停止播放音樂
async def stop(ctx, bot):
    voice_channel = get(bot.voice_clients, guild=ctx.guild)
    
    if voice_channel.is_playing():
        voice_channel.stop()

    await ctx.respond(embed=discord.Embed(
        description= f"已終止所有播放",
        color= discord.Colour.random(),
    ))