import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=('+'))
bot.remove_command( 'help' )

bot.load_extension('Bot.command_cog')
bot.load_extension('Bot.info_cog')
bot.load_extension('Bot.game_cog')

bot.run('ODMxNzA4Nzc0NTA2NTYxNTM3.YHZLKA.6gVpSsXdE-ozuPOlf1eQbGqo9W4')