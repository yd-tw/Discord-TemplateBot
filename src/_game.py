import discord
import random

async def percent(ctx,text):
    probability = random.uniform(0,100)
    await ctx.respond(embed=discord.Embed(
        title=f"{text}",
        description=f"機率為: {probability:.2f}%",
        color=discord.Colour.random(),
    ))