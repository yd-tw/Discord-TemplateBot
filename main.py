import discord
import time
import os
from dotenv import load_dotenv
import asyncio
from discord.ext import commands
from discord.utils import get

START = "%"

load_dotenv()
TOKEN = os.getenv("Token")
VERSION = os.getenv("Version")

# intents是要求機器人的權限、command_prefix是前綴符號
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = {START}, intents = intents)

#當機器人完成啟動
@bot.event 
async def on_ready():
    print(f"已成功登入:{bot.user}")

#指令列表
@bot.command()
async def list(ctx):
    options = [
        discord.SelectOption(label="基礎指令", emoji="👌", description="指令列表、學說話等基礎雜項指令"),
        discord.SelectOption(label="語音頻道", emoji="✨", description="加入、離開語音頻道"),
        discord.SelectOption(label="播放音樂", emoji="🎭", description="選擇音樂、播放、停止等..."),
        discord.SelectOption(label="設定鬧鐘", emoji="🎭", description="設定鬧鐘來吵你"),
        discord.SelectOption(label="小小遊戲", emoji="🎭", description="我還在開發，等等我QQ")
    ]

    text = {
        "基礎指令": f"基礎指令:\n```指令列表 {START}list```\n```學你說話 {START}say```\n```邀請機器人 {START}invite```",
        "語音頻道": f"語音頻道:\n```加入語音 {START}join```\n```離開語音 {START}leave```",
        "播放音樂": f"播放音樂:\n```音樂列表 {START}music```\n```播放音樂 {START}play(主檔名)\n停止播放 {START}stop```",
        "設定鬧鐘": f"設定鬧鐘:\n```設定鬧鐘 {START}alert(Year/Mon/Dat-H:M:S\)```",
        "小小遊戲": f"小小遊戲:\n就跟你說我還在開發了...不要著急啦"
    }

    view = discord.ui.View()
    select = discord.ui.Select(placeholder="選擇指令類別", max_values=1, min_values=1, options=options)

    async def select_callback(interaction: discord.Interaction):
        await interaction.response.send_message(text[interaction.data['values'][0]])

    select.callback = select_callback
    view.add_item(select)
    await ctx.send("點擊選單，查找你想要的指令~", view=view)

#文字互動
@bot.command()
async def say(ctx, text):
    await ctx.send(text)

#文字互動
@bot.command()
async def testbot(ctx):
    print(ctx)

#文字互動
@bot.command()
async def version(ctx):
    await ctx.send("當前版本:" + VERSION)

#文字互動
@bot.command()
async def invite(ctx):
    await ctx.send("https://discord.com/oauth2/authorize?client_id=1145187780364869651&permissions=0&scope=bot")

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
        await asyncio.sleep(1)

bot.run(TOKEN)