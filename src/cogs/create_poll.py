import discord

from discord.ext import commands
from discord import app_commands
from utils.embeds import make_embed

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="create_poll", description="Pong!")
    async def create_poll(self, interaction: discord.Interaction, question: str, option1: str, option2: str, option3: str | None = None, option4: str | None = None):
        options = [option1, option2]
        number_emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣"]

        if option3:
            options.append(option3)
        
        if option4:
            options.append(option4)

        response = make_embed(
            title="Create Poll",
            content=question,
            why="success"
        )

        message = await interaction.response.send_message(embed=response)
        message = await interaction.original_response()

        for i in range(len(options)):
            await message.add_reaction(number_emojis[i])

async def setup(bot):
    await bot.add_cog(Poll(bot))