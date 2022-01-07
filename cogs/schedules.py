from discord import Embed
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext
from os import environ

def getGuilds():
    guildList = environ.get('GUILD')
    guilds = []
    if guildList is not None:
        guilds.append(int(guildList.split(',')))
    return guilds

class Schedules(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @cog_ext.cog_slash(name="test", guild_ids=getGuilds())
    async def _test(self, ctx: SlashContext):
        embed = Embed(title="Embed Test")
        await ctx.send(embed=embed)

def setup(bot: Bot):
    bot.add_cog(Schedules(bot))

