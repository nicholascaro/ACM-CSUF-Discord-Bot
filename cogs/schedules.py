from discord import Embed
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext
from os import path
import json
from helpers import getGuilds
import discord

guild_ids = getGuilds()

classes_path = path.relpath("data/classes.json")
students_path = path.relpath("data/students.json")

class Schedules(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @cog_ext.cog_subcommand(base="schedule", name="view", description="View your schedule", guild_ids=guild_ids)
    async def _schedule_view(self, ctx: SlashContext):
        embed=discord.Embed(title="Hello " + ctx.author.display_name + "!", 
    description="Here are your classes:", 
    color=0xFF5733)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        classes = students[ctx.author.display_name]
        for class_name in classes:
            idx = class_name.index("-")
            class_session = class_name[idx+1:]
            embed.add_field(name=class_name[:idx], value="Session: " + class_session, inline=False)
        await ctx.send(embed=embed)

    @cog_ext.cog_subcommand(base="schedule", name="add", description="Add a class to your schedule", guild_ids=guild_ids)
    async def _schedule_add(self, ctx: SlashContext, text: str):
        await ctx.send(content="schedule add")

    @cog_ext.cog_subcommand(base="schedule", name="remove", description="Remove a class from your schedule", guild_ids=guild_ids)
    async def _schedule_remove(self, ctx: SlashContext, text: str):
        await ctx.send(content="schedule remove")

def setup(bot: Bot):
    bot.add_cog(Schedules(bot))
