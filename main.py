import os
import logging as log
import discord
from dotenv import load_dotenv

from src import *

load_dotenv()
TOKEN = os.getenv("Token")
VERSION = os.getenv("Version")
MUSICPATH = os.getenv("MusicPath")

FORMAT = "%(asctime)s %(levelname)s: %(message)s"
log.basicConfig(level=log.DEBUG, filename=".log", filemode="a", format=FORMAT, encoding="utf-8")

# intents是要求機器人的權限
intents = discord.Intents.all()
bot = discord.Bot(intents=intents)

#當機器人完成啟動
@bot.event
async def on_ready():
    print(f"已成功啟動:{bot.user}")

#指令查詢
@bot.command(name="help",description="取得指令介紹及使用幫助")
async def help(
    ctx: discord.ApplicationContext,
):
    await _help.help(ctx)

@bot.command(name="say",description="讓機器人幫你說話")
async def say(
    ctx: discord.ApplicationContext,
    text: discord.Option(str, "要讓機器人說的話", required=1),
    times: discord.Option(int, "總共要說的次數", required=0) = 1,
    delay: discord.Option(float, "每次的間隔", required=0) = 0.5,
):
    await _talk.say(ctx, text, times, delay)

@bot.command(name="version",description="顯示機器人版本")
async def version(
    ctx: discord.ApplicationContext,
):
    await _talk.version(ctx, VERSION)

@bot.command(name="invite",description="取得機器人邀請連結")
async def invite(
    ctx: discord.ApplicationContext,
):
    await _talk.invite(ctx)

@bot.command(name="ping",description="取得機器人延遲")
async def ping(
    ctx: discord.ApplicationContext,
):
    await _talk.ping(ctx, bot)

@bot.command(name="join",description="加入語音頻道")
async def join(
    ctx: discord.ApplicationContext,
):
    await _voice.join(ctx)

@bot.command(name="leave",description="離開語音頻道")
async def leave(
    ctx: discord.ApplicationContext,
):
    await _voice.leave(ctx)

@bot.command(name="musicfile",description="顯示音樂列表")
async def musicfile(
    ctx: discord.ApplicationContext,
):
    await _music.musicfile(ctx)

@bot.command(name="musicplay",description="播放音樂")
async def musicplay(
    ctx: discord.ApplicationContext, 
    file: discord.Option(str, "檔案名稱，可使用/musicfile查看列表", required=1),
):
    await _music.musicplay(ctx, file, bot, MUSICPATH)

@bot.command(name="stop",description="停止播放音樂")
async def stop(
    ctx: discord.ApplicationContext,
):
    await _music.stop(ctx, bot)

@bot.command(name="settime",description="設定鬧鐘")
async def settime(
    ctx: discord.ApplicationContext, 
    time: discord.Option(str, "輸入要設定的時間，格式為%Y/%m/%d-%H:%M:%S", required=1),
):
    await _alert.settime(ctx, time)

@bot.command(name="percent",description="說一句話，回覆你機率")
async def percent(
    ctx: discord.ApplicationContext,
    text: discord.Option(str, "輸入希望顯示機率的文字", required=True),
):
    await _game.percent(ctx, text)

if __name__ == "__main__":
    bot.run(TOKEN)