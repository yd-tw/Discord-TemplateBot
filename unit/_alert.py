import asyncio
from datetime import datetime

bell = "./music/01.mp3"

async def settime(ctx, time):
    try:
        alarm_time = datetime.strptime(time, '%Y/%m/%d-%H:%M:%S')
        seconds_until_alarm = (alarm_time - datetime.now()).total_seconds()

        if seconds_until_alarm > 0:
            await ctx.send(f'鬧鐘已設定在 {time}！')
            await asyncio.sleep(seconds_until_alarm)
            await ctx.send(f'{ctx.author.mention}，時間到了！鬧鐘觸發了！')
        else:
            await ctx.send('請輸入未來的時間！')

    except ValueError:
        await ctx.send('請使用正確的時間格式：%Y/%m/%d-%H:%M:%S')