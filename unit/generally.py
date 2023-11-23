async def say(ctx, text, times):
    if times > 10:
        return
    for i in range(times):
        await ctx.send(text)

async def version(ctx,VERSION):
    await ctx.send("當前版本:" + VERSION)

async def invite(ctx):
    await ctx.send("https://discord.com/oauth2/authorize?client_id=1145187780364869651&permissions=0&scope=bot")