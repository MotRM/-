import discord
from discord.ext import commands

class Bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Я запущен!")

    @commands.command()
    async def Привет(self, ctx):
        await ctx.send('Привет! Я бот для игры в города. Если хочешь сыграть набери +Игра')

    @commands.command(pass_context=True)
    async def Чистка(self, ctx, amount=100):
        await ctx.channel.purge(limit=amount)

def setup(bot):
    bot.add_cog(Bot(bot))