#加入語音頻道
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send(f'加入了語音頻道 {channel}')

#離開語音頻道
async def leave(ctx):
    channel = ctx.author.voice.channel
    await ctx.voice_client.disconnect()
    await ctx.send(f'被趕出語音頻道 {channel}')