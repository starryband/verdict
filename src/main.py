import os
import discord

from utils.embeds import make_embed
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

    try:
        for cog in os.listdir('src/cogs'):
            if cog.endswith('.py') and cog != "__init__.py":
                await bot.load_extension(f'cogs.{cog[:-3]}')
        print("loaded cogs")
    except Exception as e:
        print(f'failed to load cogs: {e}')

    await bot.tree.sync()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass
    else:
        embed = make_embed(
            title="Error Occurred",
            content=str(error),
            why="error"
        )
        await ctx.send(embed=embed)

bot.run(token=DISCORD_TOKEN)