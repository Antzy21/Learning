import discord
from discord.ext import commands
from discord.ext.commands import Bot
from Ids import *

bot = discord.Client()

@bot.event
async def on_ready():
    print("\nI am running on", bot.user.name)
    print("With the ID", bot.user.id)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
        
    print(f'{message.channel}: {message.author.name}: {message.content}')

    if 'hi' in message.content.lower():
        await message.channel.send('hi')

    if 'bye' == message.content.lower():
        await bot.close()


bot.run(TOKEN) 