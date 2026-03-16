import discord

from discord.ext import commands
from discord import app_commands
from utils.embeds import make_embed

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Pong!")
    async def ping(self, interaction: discord.Interaction):
        try:
            response = make_embed("Ping", "Pong!", "success")
        except Exception as e:
            response = make_embed("Error Occured", f"{e}", "error")
        await interaction.response.send_message(embed=response)

async def setup(bot):
    await bot.add_cog(Ping(bot))