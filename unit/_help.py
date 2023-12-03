import discord

async def help(ctx):
    options = [
        discord.SelectOption(label="基礎指令", emoji="👌", description="邀請連結、學說話、機器人資訊等......"),
        discord.SelectOption(label="語音頻道", emoji="✨", description="加入、離開語音頻道"),
        discord.SelectOption(label="播放音樂", emoji="🎭", description="選擇音樂、播放、停止等......"),
        discord.SelectOption(label="設定鬧鐘", emoji="🎭", description="設定鬧鐘來吵你"),
        discord.SelectOption(label="小小遊戲", emoji="🎭", description="我還在開發，等等我 QAQ")
    ]

    text = {
        "基礎指令": f"基礎指令:\
        \n```學你說話 /say(要說的話,次數,間隔秒數)```\
        \n```邀請機器人 /invite```\
        \n```查詢延遲 /ping```\
        \n```機器人版本 /version```",
        "語音頻道": f"語音頻道:\
        \n```加入語音 /join```\
        \n```離開語音 /leave```",
        "播放音樂": f"播放音樂:\
        \n```音樂列表 /music```\
        \n```播放音樂 /play(主檔名)\
        \n停止播放 /stop```",
        "設定鬧鐘": f"設定鬧鐘:\
        \n```設定鬧鐘 /alert(Year/Mon/Dat-H:M:S\)```",
        "小小遊戲": f"小小遊戲:\
        \n```機率 /QA(一個問題)"
    }

    view = discord.ui.View()
    select = discord.ui.Select(placeholder="選擇指令類別", max_values=1, min_values=1, options=options)

    async def select_callback(interaction: discord.Interaction):
        await interaction.response.send_message(text[interaction.data['values'][0]])

    select.callback = select_callback
    view.add_item(select)
    await ctx.respond("點擊選單，查找你想要的指令~", view=view)