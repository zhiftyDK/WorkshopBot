async def handle_response(message, client):
    content = str(message.content).lower().replace(f"<@{client.user.id}>", "")
    # Implement carter here :)