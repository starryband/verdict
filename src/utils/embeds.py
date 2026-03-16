import discord

def make_embed(title, content, why=None):
    colors = {
        "error": discord.Color.red(),
        "success": discord.Color.green(),
    }

    icons = { # to be used when i can figure out how to get componentsv2 working
        "error": "🔴",
        "success": "🟢",
    }

    color = colors.get(why, discord.Color.light_grey())
    icon = icons.get(why, "⚪")

    embed = discord.Embed(
        title=f"{icon} {title}",
        description=content,
        color=color
    )

    return embed