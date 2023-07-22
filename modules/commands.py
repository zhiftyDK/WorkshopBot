def handle_commands(tree, app_commands, discord, guild):

    @tree.command(name="repeat", description="Repeat text.. Permission needed!", guild=guild)
    @app_commands.describe(message="What should i repeat?")
    async def repeat(interaction, message: str):
        if discord.utils.get(interaction.guild.roles, id=1113442580391284857) in interaction.user.roles:
            await interaction.channel.send(message)
            await interaction.response.send_message("Successfully repeated your message!", ephemeral=True)
        else:
            await interaction.response.send_message(f"<@{interaction.user.id}> You dont have permission!")
    
    @tree.command(name="clear", description="Clear amount of messages.. Permission needed!", guild=guild)
    @app_commands.describe(amount="Amount of messages to clear!")
    async def clear(interaction, amount: int):
        if discord.utils.get(interaction.guild.roles, id=1113442580391284857) in interaction.user.roles:
            await interaction.response.defer(ephemeral=True)
            await interaction.channel.purge(limit=amount)
            await interaction.followup.send(f"You cleared {amount} messages!")
        else:
            await interaction.response.send_message(f"<@{interaction.user.id}> You dont have permission!")