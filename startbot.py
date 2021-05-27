import discord
from Core import gamecity, chat_user
from Bot import command_cog, info_cog, game_cog


from discord.ext import commands

bot = commands.Bot(command_prefix=('+'), help_command=None, case_insensitive=True)
bot.remove_command( 'help' )

bot.add_cog(command_cog.Bot(bot))
bot.add_cog(info_cog.Info(bot))
bot.add_cog(game_cog.Game(bot))

bot.run('')