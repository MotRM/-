import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Помощь(self, ctx):
        await ctx.send('Команды:\n'
                       '+Привет - привествие\n'
                       '+Чистка - удалить 100 сообщений\n'
                       '+Игра - запустить игру')

def setup(bot):
    bot.add_cog(Info(bot))