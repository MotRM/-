import discord
from Core import gamecity
from discord.ext import commands

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content

        if message.author == self.bot.user:
            return

        def check(msg):
            if msg.author.bot:
                return
            else:
                return msg

        if msg == '+Игра':
            await message.channel.send(gamecity.first_start_game())
            while True:
                message = await self.bot.wait_for('message', check=check)
                if message.content == '+Закончить':
                    await message.channel.send('Спасибо за игру!')
                    gamecity.clear_dict_cities()
                    return
                else:
                    await message.channel.send(gamecity.game_city(message.content))
        await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(Game(bot))