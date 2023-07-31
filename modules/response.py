async def handle_response(message, client):
    content = str(message.content).lower().replace(f"<@{client.user.id}>", "")
    await message.channel.send(f"Sorry but im currently not able to start a conversation!", reference=message)