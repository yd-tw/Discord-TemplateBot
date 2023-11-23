import random

async def QA(ctx,text):
    await ctx.send(text + ":" + random.uniform(0,100) + "%")