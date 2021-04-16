import discord
from discord.ext import commands
import gamecity

bot = commands.Bot(command_prefix=('+'))
bot.remove_command( 'help' )

@bot.event
async def on_ready():
    print("Я запущен!")

@bot.command()
async def Привет(ctx):
    await ctx.send('Привет! Я бот для игры в города. Если хочешь сыграть набери +Игра')

@bot.command()
async def Игра(ctx):
    await ctx.send(gamecity.first_start_game())


@bot.command()
async def on_message(message):
    if message.author == bot.user:
        return

bot.run('')