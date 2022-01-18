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

        # What happened to the previous code??
        # A: We decided to use 'Cogs'. Essentially, cogs allow you to organize your code with classes.
        #    You will notice we now have a 'Roles.py' file that handles all the events in our 'Roles' class
        #    And, we also have a 'Schedules.py' file that handles all the events/commands in our 'Schedules' class
        #    Although you might see slight changes, don't worry. The same logic we've learned still applies!

        # TO DO:
        # - Send a message in your #Get-Roles text channel
        # - Using 'on_raw_reaction_add' make another listener event that gives a member role depending on their
        #   reaction to the message you sent in the #Get-Roles channel
        # (For example, if the user reacts to the message with the :acmDev: emoji, then that user
        # will be added to the 'Dev Member' Role.)
        # - There are three roles they can choose to join, 'Dev Member', 'Algo Member', and 'Create Member'.

        # Steps to do this:
        # 1) Store each role into a variable using 'discord.utils.get'
        # 2)Store the id of the designated #Get-Roles message into a variable
        # 3)Check if the payload message id matches the designated #Get-Roles message id
        # 4)If they do match, use if statements to handle each of the three possible reactions
        #   (Ex.If the emoji id equal's that of the :acmDev: emoji, give them the 'Dev Member' Role)
        # 5)Use the 'add_roles' function to add the member to a role

        # TIPS/HINTS
        # - In order to get the id of a emoji, type/enter into a text channel "\[emoji_name_goes_here"
        # - For example, if the emoji's name was 'happy' you would type/enter into a text channel
        #   '\happy'
        # - 'on_raw_reaction_add' has a payload parameter make sure to look into it
        # - All of the functions I mentioned are explained in the Discord.py API Reference

    @Cog.listener()
    async def on_raw_reaction_add(self, payload):
        # YOUR CODE GOES HERE
<<<<<<< HEAD
=======
        pass
    
>>>>>>> e69a1eb375a3a12730628cb27a64f58a88211e85

        devM = discord.utils.get(
            payload.member.guild.roles, id=916198780754346017)
        algoM = discord.utils.get(
            payload.member.guild.roles, id=916198780754346018)
        createM = discord.utils.get(
            payload.member.guild.roles, id=916198780754346019)

        emojiID = {'dev': 930209176431505509,
                   'algo': 930209120907296799, 'create': 930209148543578213}

        role_message_id = 932456799607599144

        if payload.message_id == role_message_id:
            if payload.emoji_id == emojiID['dev']:
                await payload.member.add_roles(devM)
            elif payload.emoji_id == emojiID['algo']:
                await payload.member.add_roles(algoM)
            elif payload.emoji_id == emojiID['create']:
                await payload.member.add_roles(createM)


def setup(bot: Bot):
    bot.add_cog(Roles(bot))
