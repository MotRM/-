from discord.ext import commands
import gamecity

bot = commands.Bot(command_prefix=('+'))
bot.remove_command( 'help' )

@bot.event
async def on_ready():
    print("Я запущен!")

@bot.command()
async def Привет(ctx):
    await ctx.send('Привет! Я бот для игры в города. Если хочешь сыграть набери Игра')

@bot.command(pass_context=True)
async def Чистка(ctx, amount=100):
    await ctx.channel.purge(limit=amount)

@bot.event
async def on_message(message):
    msg = message.content

    if message.author == bot.user:
        return

    def check(msg):
        if msg.author.bot:
            return
        else:
            return msg

    if msg == 'Игра':
        await message.channel.send(gamecity.first_start_game())
        while True:
            message = await bot.wait_for('message', check=check)
            if message.content == 'Закончить':
                await message.channel.send('Спасибо за игру!')
                gamecity.clear_dict_cities()
                return
            else:
                await message.channel.send(gamecity.game_city(message.content))

    await bot.process_commands(message)

bot.run('ODMxNzA4Nzc0NTA2NTYxNTM3.YHZLKA.5STcmYiWfQBGyPYP_e3KID6UrbU')