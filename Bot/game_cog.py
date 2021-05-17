from Core.chat_user import CityGameSession, all_user_list
from discord.ext import commands
from Core.gamecity import first_start_game, game_city, clear_dict_cities


class Game(commands.Cog):
    '''
    Данный Cog содержит в себе event on_message. Event
    запускает игровую сейссию, когда в чате появляется
    сообщение Игра. Одна игровая сейссия длится до победы
    игрока или пока игрок не наберет сообщение Закончить
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        ch_id = message.channel.id
        user_id = message.author.id
        game_session = False

        if message.author == self.bot.user:
            return

        if ch_id in all_user_list:
            return
        else:
            all_user_list[ch_id] = CityGameSession(ch_id, user_id, game_session)
            print(all_user_list)

        if all_user_list[ch_id].game_session:
            await message.channel.send((game_city(message.content,
                                                  all_user_list[ch_id].dict_cities)))

        if message.content == 'Игра':
            if all_user_list[ch_id].game_session:
                await message.channel.send('Вы уже играете!')
            else:
                all_user_list[ch_id].game_session = True
                print(all_user_list)
                await message.channel.send(first_start_game(all_user_list[ch_id].dict_cities))

        if message.content == 'Закончить':
            all_user_list[ch_id].game_session = False
            print(all_user_list)
            await message.channel.send('Спасибо за игру!')
            clear_dict_cities(all_user_list[ch_id].dict_cities)

        print(message.content)