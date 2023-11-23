import random

async def QA(ctx,text):
    await ctx.send(text + " 機率為: " + str(random.uniform(0,100)) + "%")