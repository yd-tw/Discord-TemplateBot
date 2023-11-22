import discord
import time
from discord.ext import commands
from discord.utils import get

START = "%"

# intents是要求機器人的權限
intents = discord.Intents.all()
# command_prefix是前綴符號，可以自由選擇
bot = commands.Bot(command_prefix = {START}, intents = intents)

#當機器人完成啟動
@bot.event 
async def on_ready():
    print(f"已成功登入:{bot.user}")

#指令列表
@bot.command()
async def list(ctx):
    await ctx.send(f"\
指令列表:\n\
1. 調用指令列表 {START}list\n\
2. 學說話 {START}say\n\
3. 加入語音頻道 {START}join\n\
4. 離開語音頻道 {START}leave\n\
5. 音樂列表 {START}music\n\
5. 播放音樂 {START}play (主檔名)\n\
6. 停止播放 {START}stop\n\
7. 設定鬧鐘 {START}alert (Year/Mon/Dat-H:M:S\)\n\
                   ")

#文字互動
@bot.command()
async def say(ctx, text):
    await ctx.send(text)

#加入語音頻道
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send(f'加入了語音頻道 {channel}')

#離開語音頻道
@bot.command()
async def leave(ctx):
    channel = ctx.author.voice.channel
    await ctx.voice_client.disconnect()
    await ctx.send(f'被趕出語音頻道 {channel}')

#音樂列表
@bot.command()
async def music(ctx):
    await ctx.send("音樂曲目名稱:\n01\n02\n03\n04")

#播放本地音樂
@bot.command()
async def play(ctx, file_name):
    file_name = "music/" + file_name + ".mp3"
    voice_channel = get(bot.voice_clients, guild=ctx.guild)
    
    if voice_channel.is_playing():
        await ctx.send(f"音频正在播放，請先使用{START}stop停止")
    else:
        voice_channel.play(discord.FFmpegPCMAudio(file_name))
        await ctx.send(f"正在播放{file_name}")

#停止播放音樂
@bot.command()
async def stop(ctx):
    voice_channel = get(bot.voice_clients, guild=ctx.guild)
    
    if voice_channel.is_playing():
        voice_channel.stop()

#鬧鐘(運行時不能執行其他指令)
@bot.command()
async def alert(ctx, alarm_time):
    bell = "music/01.mp3"
    await ctx.send(f'已設定時間{alarm_time}\n鈴聲設定為{bell}')

    while 1:
        now_time = time.strftime('%Y/%m/%d-%H:%M:%S',time.localtime())
        print(now_time,alarm_time)

        if now_time == alarm_time:
            voice_channel = get(bot.voice_clients, guild=ctx.guild)
            if voice_channel.is_playing():
                voice_channel.stop()
                voice_channel.play(discord.FFmpegPCMAudio(bell))
            else:
                voice_channel.play(discord.FFmpegPCMAudio(bell))
            await ctx.send('時間到了!')
            break
        time.sleep(1)

bot.run("MTE0NTE4Nzc4MDM2NDg2OTY1MQ.GSiJ3A.QjB2Koi73L5YLCUOCun3fvejiUk-mK5bnM42uM")