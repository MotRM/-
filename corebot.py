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

@bot.command(pass_context=True)
async def Чистка(ctx, amount=100):
    await ctx.channel.purge(limit=amount)

@bot.event
async def on_message(message):
    msg = message.content

    if message.author == bot.user:
        return

    if msg == 'Игра':
        @bot.event
        async def on_message(message):
            if message.author == bot.user:
                return
            await message.channel.send(gamecity.game_city(message.content))

    await bot.process_commands(message)
bot.run('')