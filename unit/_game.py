import random

async def qa(ctx,text):
    random.seed(text)
    probability = random.uniform(0,100)
    await ctx.respond(f"{text}機率為: {probability:.2f}%")