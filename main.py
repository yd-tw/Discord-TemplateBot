import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

from unit import *

load_dotenv()
START = os.getenv("Start")
TOKEN = os.getenv("Token")

VERSION = os.getenv("Version")

MUSICPATH = os.getenv("MusicPath")

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
    await _help.help(ctx,START)


#複述對話
@bot.command()
async def say(ctx, text, times: int = 1, delay: int = 0):
    print("say")
    await _talk.say(ctx, text, times, delay)
#版本查詢
@bot.command()
async def version(ctx):
    print("version")
    await _talk.version(ctx, VERSION)
#邀請連結
@bot.command()
async def invite(ctx):
    print("invite")
    await _talk.invite(ctx)
#取得延遲
@bot.command()
async def ping(ctx):
    await _talk.ping(ctx, bot)


#加入語音
@bot.command()
async def join(ctx):
    print("join")
    await _voice.join(ctx)
#離開語音
@bot.command()
async def leave(ctx):
    print("leave")
    await _voice.leave(ctx)


#音樂列表
@bot.command()
async def list(ctx):
    print("list")
    await _music.list(ctx)
#播放本地音樂
@bot.command()
async def play(ctx, file):
    print("play")
    await _music.play(ctx, file, bot, START, MUSICPATH)
#停止播放音樂
@bot.command()
async def stop(ctx):
    print("stop")
    await _music.stop(ctx, bot)


#設定鬧鐘
@bot.command()
async def settime(ctx, time):
    print("settime")
    await _alert.settime(ctx, time)


#遊戲
@bot.command()
async def QA(ctx, text):
    print("QA")
    await _game.QA(ctx, text)

bot.run(TOKEN)