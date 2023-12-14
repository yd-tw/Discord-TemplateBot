import discord
import asyncio

async def say(ctx, text, times, delay):
    if times > 50:
        await ctx.respond(embed=discord.Embed(
            description= "到底是誰同意你輸入這麼大的數字?",
            color= discord.Colour.random(),
        ))
    else:
        await ctx.respond(embed=discord.Embed(
            description= "訊息已受理",
            color= discord.Colour.random(),
        ))
        for _ in range(times):
            await ctx.send(text)
            await asyncio.sleep(delay)

async def version(ctx, VERSION):
    await ctx.respond(embed=discord.Embed(
        description= f"當前版本: {VERSION}",
        color= discord.Colour.random(),
    ))

async def invite(ctx):
    await ctx.respond(embed=discord.Embed(
        description= "邀我到其他伺服器!!!\nhttps://discord.com/oauth2/authorize?client_id=1145187780364869651&permissions=0&scope=bot",
        color= discord.Colour.random(),
    ))

async def ping(ctx, bot):
    latency = bot.latency * 1000  # 將延遲轉換為毫秒
    await ctx.respond(embed=discord.Embed(
        description= f'機器人延遲為 {latency:.2f} 毫秒',
        color= discord.Colour.random(),
    ))