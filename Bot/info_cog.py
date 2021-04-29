import discord
from discord.ext import commands

class Info(commands.Cog):
    '''
    Данный Cog содержит в себе следующие команды для получения информации:
    Помощь - отражает набор всех команд в боте
    Правила - отражает сообщение с правилами игры (не реализован)
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Помощь(self, ctx):
        await ctx.send('Команды:\n'
                       '+Привет - привествие\n'
                       '+Чистка - удалить 100 сообщений\n'
                       'Игра - запустить игру')

def setup(bot):
    bot.add_cog(Info(bot))