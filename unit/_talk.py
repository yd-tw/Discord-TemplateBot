import asyncio

async def say(ctx, text, times, delay):
    if times > 100:
        await ctx.send("到底是誰同意你輸入這麼大的數字?")
        return
    for _ in range(times):
        await ctx.send(text)
        await asyncio.sleep(delay)

async def version(ctx,VERSION):
    await ctx.send("當前版本:" + VERSION)

async def invite(ctx):
    await ctx.send("邀我到其他伺服器!!!\nhttps://discord.com/oauth2/authorize?client_id=1145187780364869651&permissions=0&scope=bot")

async def ping(ctx, bot):
    latency = bot.latency * 1000  # 將延遲轉換為毫秒
    await ctx.send(f'機器人延遲為 {latency:.2f} 毫秒')