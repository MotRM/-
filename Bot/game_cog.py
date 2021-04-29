import discord
from Core import gamecity, chat_user
from discord.ext import commands

class Game(commands.Cog):

    '''
    Данный Cog содержит в себе event on_message. Event
    запускает игровую сейссию, когда в чате появляется
    сообщение +Игра. Одна игровая сейссия длится до победы
    игрока или пока игрок не наберет сообщение +Закончить
    '''

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content
        ch_id = message.channel.id
        user_id = message.author.id

        if message.author == self.bot.user:
            return

        def check(msg):
            if msg.author.bot:
                return
            else:
                return msg

        if ch_id in chat_user.chat_id_list:
            return
        else:
            chat_user.chat_id_list[ch_id] = chat_user.Chat_user(ch_id, user_id)

        print(chat_user.chat_id_list)
        print(chat_user.chat_id_list[ch_id].dict_cities)

        if msg == 'Игра':
            await message.channel.send(gamecity.first_start_game(chat_user.chat_id_list[ch_id].dict_cities))
            while True:
                message = await self.bot.wait_for('message', check=check)
                if message.content == 'Закончить':
                    await message.channel.send('Спасибо за игру!')
                    gamecity.clear_dict_cities(chat_user.chat_id_list[ch_id].dict_cities)
                    return
                else:
                    await message.channel.send((gamecity.game_city(message.content,
                                                                  chat_user.chat_id_list[ch_id].dict_cities)))

def setup(bot):
    bot.add_cog(Game(bot))