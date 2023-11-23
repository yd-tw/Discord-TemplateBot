import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

from unit import helpcode
from unit import generally
from unit import voice
from unit import music
from unit import alert

load_dotenv()
TOKEN = os.getenv("Token")
VERSION = os.getenv("Version")
START = "%"

# intents是要求機器人的權限、command_prefix是前綴符號
bot = commands.Bot(command_prefix = {START}, intents = discord.Intents.all())

bot.help_command = None

#當機器人完成啟動
@bot.event 
async def on_ready():
    print(f"已成功登入:{bot.user}")

#指令查詢
@bot.command()
async def help(ctx, argument=None):
    print("help")
    await helpcode.help(ctx,START)


#複述對話
@bot.command()
async def say(ctx, text, times: int = 1):
    print("say")
    await generally.say(ctx,text,times)
#版本查詢
@bot.command()
async def version(ctx):
    print("version")
    await generally.version(ctx,VERSION)
#邀請連結
@bot.command()
async def invite(ctx):
    print("invite")
    await generally.invite(ctx)


#加入語音
@bot.command()
async def join(ctx):
    print("join")
    await voice.join(ctx)
#離開語音
@bot.command()
async def leave(ctx):
    print("leave")
    await voice.leave(ctx)


#音樂列表
@bot.command()
async def list(ctx):
    print("list")
    await music.list(ctx)
#播放本地音樂
@bot.command()
async def play(ctx, file_name):
    print("play")
    await music.play(ctx, file_name, bot, START)
#停止播放音樂
@bot.command()
async def stop(ctx):
    print("stop")
    await music.stop(ctx, bot)


#設定鬧鐘
@bot.command()
async def settime(ctx, time):
    print("settime")
    await alert.settime(ctx, time)

bot.run(TOKEN)