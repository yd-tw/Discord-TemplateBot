# 導入Discord.py模組
import discord
# 導入commands指令模組
from discord.ext import commands

# intents是要求機器人的權限
intents = discord.Intents.all()
# command_prefix是前綴符號，可以自由選擇($, #, &...)
bot = commands.Bot(command_prefix = "%", intents = intents)

@bot.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.command()
# 輸入%Hello呼叫指令
async def Hello(ctx):
    # 回覆Hello, world!
    await ctx.send("Hello, world!")

@bot.command()
async def join(ctx):
    # 獲取語音頻道
    channel = ctx.author.voice.channel

    # 如果機器人已經在語音頻道中，則不執行任何操作
    if ctx.voice_client is not None:
        return await ctx.voice_client.move_to(channel)

    # 加入語音頻道
    await channel.connect()
    await ctx.send(f'加入了語音頻道 {channel}')

@bot.command()
async def leave(ctx):
    # 如果機器人不在語音頻道中，則不執行任何操作
    if ctx.voice_client is None:
        return await ctx.send('我不在任何語音頻道中。')

    # 離開語音頻道
    await ctx.voice_client.disconnect()
    await ctx.send('離開了語音頻道。')

bot.run("MTE0NTE4Nzc4MDM2NDg2OTY1MQ.GSiJ3A.QjB2Koi73L5YLCUOCun3fvejiUk-mK5bnM42uM")