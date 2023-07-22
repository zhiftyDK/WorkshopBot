async def handle_badwords(message):
    if not "1113442580391284857" in str(message.author.roles) and not "1132369442836316180" in str(message.author.roles):
        with open("modules/badwords.txt", "r", encoding="utf-8") as f:
            for badword in f.readlines():
                if badword.lower().strip() in message.content.lower():
                    await message.delete()
                    await message.channel.send(f"<@{message.author.id}> We dont tollerate this kind of language!")