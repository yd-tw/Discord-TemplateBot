import discord

#加入語音頻道
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.respond(embed=discord.Embed(
        description= f'加入了語音頻道 {channel}',
        color= discord.Colour.random(),
    ))
    

#離開語音頻道
async def leave(ctx):
    channel = ctx.author.voice.channel
    await ctx.voice_client.disconnect()
    await ctx.respond(embed=discord.Embed(
        description= f"被趕出 {channel} 了，嗚嗚",
        color= discord.Colour.random(),
    ))