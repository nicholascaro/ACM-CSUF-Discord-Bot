from discord.ext.commands import Bot, Cog
import os
import discord
from discord.ext.commands.converter import TextChannelConverter
from dotenv import load_dotenv
load_dotenv()


class Roles(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

    @Cog.listener()
    async def on_message(self, message):
        if message.content == "Hi":
            await message.channel.send("Hello")

    @Cog.listener()
    async def on_member_join(self, member):
        # NEWCOMER is the id of the NewComer role in my server
        role = discord.utils.get(
            member.guild.roles, id=int(os.environ.get('NEWCOMER')))
        await member.add_roles(role)

    @Cog.listener()
    async def on_raw_reaction_add(self, payload):

        member = payload.member

        dev_role = discord.utils.get(
            # token is for the id of the 'Dev Member' role
            member.guild.roles, id=int(os.environ.get('DEV')))
        algo_role = discord.utils.get(
            # token is for the id of the 'Algo Member' role
            member.guild.roles, id=int(os.environ.get('ALGO')))
        create_role = discord.utils.get(
            member.guild.roles, id=int(os.environ.get('CREATE')))

        emoji_id = payload.emoji.id
        role_message_id = 933135629624156191  # using a random message ID to test

        if payload.message_id == role_message_id:
            # token is for the dev emoji ID
            if emoji_id == int(os.environ.get('DEVEMOJI')):
                await member.add_roles(dev_role)
            # token is for the algo emoji ID
            elif emoji_id == int(os.environ.get('ALGOEMOJI')):
                await member.add_roles(algo_role)
            # token is for the create emoji ID
            elif emoji_id == int(os.environ.get('CREATEEMOJI')):
                await member.add_roles(create_role)

        # TO DO:
        # - Add all the previously mentioned .env variables ('NEWCOMER','DEV','DEVEMOJI', etc.)
        # - Create an event using 'on_raw_reaction_remove'
        # - Make the event so that when a user removes their reaction from the #Get-Roles message,
        #   that relateD role is removed
        # - For example, if a user removes their :acmDev: reaction from the #Get-Roles message, then they
        #   will no longer have the 'Dev Member' role

        # HINTS/NOTES:
        # - Although you may think you can simply just use the code for the 'on_raw_reaction_add' event and switch out the
        #   'add_roles' function for the 'remove_roles' function, it is not that simple
        # - Note that 'on_raw_reaction_remove' doesn't allow you to retrieve the member attribute so we'll need to work around this

        # STEPS:
        # 1)Store the current guild in a variable using the 'fetch_guild' function
        # 2)Store the member who reacted in a variable using the 'fetch_member' function
        # 3)Now that you have access to the guild, use the 'get_role' function to store each role
        #   into their respective Variable
        # 4)Similarly to the 'on_raw_reaction_add' event , get the message id of the #Get-Roles message and store it into a variable
        # 5)Similarly to the 'on_raw_reaction_add' event, create a check to make sure our event only responds to the #Get-Roles message
        # 6)Similarly to the 'on_raw_reaction_add' event, create if statements for each of the three roles and use the 'remove_roles' function
        #   to remove the respective role

    @Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        curr_guild = await self.bot.fetch_guild(payload.guild_id)
        member = await curr_guild.fetch_member(payload.user_id)
        message_id = 933135629624156191
        dev_role = curr_guild.get_role(int(os.environ.get('DEV')))
        algo_role = curr_guild.get_role(int(os.environ.get('ALGO')))
        create_role = curr_guild.get_role(int(os.environ.get('CREATE')))
        emoji = payload.emoji.id
        if payload.message_id == message_id:
            if emoji == int(os.environ.get('DEVEMOJI')):
                await member.remove_roles(dev_role)
                print(f"Dev Role removed from -> {member.display_name}")
        # token is for the algo emoji ID
            elif emoji == int(os.environ.get('ALGOEMOJI')):
                await member.remove_roles(algo_role)
                print(f"Algo Role removed from -> {member.display_name}")
            # token is for the create emoji ID
            elif emoji == int(os.environ.get('CREATEEMOJI')):
                await member.remove_roles(create_role)
                print(f"Create Role removed from -> {member.display_name}")
        # YOUR CODE HERE---------------------------------


def setup(bot: Bot):
    bot.add_cog(Roles(bot))
