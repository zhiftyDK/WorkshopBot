from modules.textgeneration import generate
async def handle_response(message, client):
    content = str(message.content).lower().replace(f"<@{client.user.id}>", "")
    output = generate(prompt=content, system_prompt="You are an AI assistant, you are 25 years old and love to help people")
    await message.channel.send(output, reference=message)