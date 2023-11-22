import discord
from discord.ext import commands
from discord.utils import get

# intents是要求機器人的權限
intents = discord.Intents.all()
# command_prefix是前綴符號，可以自由選擇
bot = commands.Bot(command_prefix = "%", intents = intents)


#當機器人完成啟動
@bot.event 
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

# 輸入%Hello呼叫指令
async def Hello(ctx):
    await ctx.send("Hello, world!")

# 加入語音頻道的命令
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send(f'加入了語音頻道 {channel}')

# 播放本地音频文件的命令
@bot.command()
async def play(ctx, file_name):
    voice_channel = get(bot.voice_clients, guild=ctx.guild)
    
    if not voice_channel.is_playing():
        audio_source = discord.FFmpegPCMAudio(file_name)
        voice_channel.play(audio_source)
    else:
        await ctx.send("音频正在播放")

# 停止播放的命令
@bot.command()
async def stop(ctx):
    voice_channel = get(bot.voice_clients, guild=ctx.guild)
    
    if voice_channel.is_playing():
        voice_channel.stop()

# 断开连接的命令
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    await ctx.send('離開了語音頻道。')

# 运行Bot
bot.run("MTE0NTE4Nzc4MDM2NDg2OTY1MQ.GSiJ3A.QjB2Koi73L5YLCUOCun3fvejiUk-mK5bnM42uM")