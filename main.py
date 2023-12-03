import os
import logging as log
import discord
from dotenv import load_dotenv

from unit import *

load_dotenv()
TOKEN = os.getenv("Token")
VERSION = os.getenv("Version")
MUSICPATH = os.getenv("MusicPath")

FORMAT = '%(asctime)s %(levelname)s: %(message)s'
log.basicConfig(level=log.DEBUG, filename='.log', filemode='a', format=FORMAT, encoding='utf-8')

# intents是要求機器人的權限、command_prefix是前綴符號
intents = discord.Intents.all()
bot = discord.Bot(intents=intents)
bot.help_command = None

#當機器人完成啟動
@bot.event
async def on_ready():
    print(f"已成功啟動:{bot.user}")

#指令查詢
@bot.command()
async def help(ctx, argument=None):
    await _help.help(ctx)


@bot.command(name="say",description="讓機器人幫你說話")
async def say(
    ctx, 
    text, 
    times: int = 1, 
    delay: int = 0
):
    await _talk.say(ctx, text, times, delay)

@bot.command(name="version",description="顯示機器人版本")
async def version(
    ctx
):
    await _talk.version(ctx, VERSION)

@bot.command(name="invite",description="取得機器人邀請連結")
async def invite(
    ctx
):
    await _talk.invite(ctx)

@bot.command(name="ping",description="取得機器人延遲")
async def ping(
    ctx
):
    await _talk.ping(ctx, bot)


@bot.command(name="join",description="加入語音頻道")
async def join(
    ctx
):
    await _voice.join(ctx)

@bot.command(name="leave",description="離開語音頻道")
async def leave(
    ctx
):
    await _voice.leave(ctx)


@bot.command(name="list",description="顯示音樂列表")
async def list(
    ctx
):
    await _music.list(ctx)

@bot.command(name="play",description="播放音樂")
async def play(
    ctx, 
    file
):
    await _music.play(ctx, file, bot, MUSICPATH)

@bot.command(name="stop",description="停止播放音樂")
async def stop(
    ctx
):
    await _music.stop(ctx, bot)


@bot.command(name="settime",description="設定鬧鐘")
async def settime(
    ctx, 
    time
):
    await _alert.settime(ctx, time)


@bot.command(name="percent",description="說一句話，回覆你機率")
async def qa(
    ctx,
    text: discord.Option(str, "輸入希望顯示機率的文字", required=True)
):
    await _game.qa(ctx, text)

if __name__ == "__main__":
    bot.run(TOKEN)