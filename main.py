import os
import logging as log
import discord
from dotenv import load_dotenv

from unit import *

load_dotenv()
START = os.getenv("Start")
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
    print(f"已成功登入:{bot.user}")

# @bot.event
# async def on_message(message):
#     await bot.process_commands(message)

#     if str(message.content)[0]==START:
#         log.info(f"{message.guild},{message.channel},{message.author},{message.content}")
#     else:
#         log.debug(f"{message.guild},{message.channel},{message.author},{message.content}")

@bot.event
async def on_command_error(ctx,error):
    log.warning(f"{ctx.guild},{ctx.channel},{ctx.author},: {error}")

#指令查詢
@bot.command()
async def help(ctx, argument=None):
    await _help.help(ctx,START)


#複述對話
@bot.command(name="say",description="讓機器人幫你說話")
async def say(ctx, text, times: int = 1, delay: int = 0):
    await _talk.say(ctx, text, times, delay)
#版本查詢
@bot.command(name="version",description="顯示機器人版本")
async def version(ctx):
    await _talk.version(ctx, VERSION)
#邀請連結
@bot.command(name="invite",description="取得機器人邀請連結")
async def invite(ctx):
    await _talk.invite(ctx)
#取得延遲
@bot.command(name="ping",description="取得機器人延遲")
async def ping(ctx):
    await _talk.ping(ctx, bot)


#加入語音
@bot.command(name="join",description="加入語音頻道")
async def join(ctx):
    await _voice.join(ctx)
#離開語音
@bot.command(name="leave",description="離開語音頻道")
async def leave(ctx):
    await _voice.leave(ctx)


#音樂列表
@bot.command(name="list",description="顯示音樂列表")
async def list(ctx):
    await _music.list(ctx)
#播放本地音樂
@bot.command(name="play",description="播放音樂")
async def play(ctx, file):
    await _music.play(ctx, file, bot, START, MUSICPATH)
#停止播放音樂
@bot.command(name="stop",description="停止播放音樂")
async def stop(ctx):
    await _music.stop(ctx, bot)


#設定鬧鐘
@bot.command(name="settime",description="設定鬧鐘")
async def settime(ctx, time):
    await _alert.settime(ctx, time)


#遊戲
@bot.command(name="percent",description="說一句話，回覆你機率")
async def qa(ctx, text: discord.Option(str, "輸入希望顯示機率的文字", required=True)):
    await _game.qa(ctx, text)

if __name__ == "__main__":
    bot.run(TOKEN)