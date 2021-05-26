from Core.chat_user import CityGameSession, all_user_list
from discord.ext import commands
from Core.gamecity import first_start_game, game_city, clear_dict_cities


class Game(commands.Cog):

    """
    Данный Cog содержит в себе event on_message. Event
    запускает игровую сейссию, когда в чате появляется
    сообщение Игра. Одна игровая сейссия длится до победы
    игрока или пока игрок не наберет сообщение Закончить
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        ch_id = message.channel.id
        user_id = message.author.id

        if message.author == self.bot.user:
            return

        if ch_id not in all_user_list:
            all_user_list[ch_id] = CityGameSession(ch_id, user_id, False)

        if message.content == "Закончить" and all_user_list[ch_id].game_session:
            all_user_list[ch_id].game_session = False
            await message.channel.send("Спасибо за игру!")
            clear_dict_cities(all_user_list[ch_id].dict_cities)
        else:
            if all_user_list[ch_id].game_session:
                await message.channel.send((game_city(message.content, all_user_list[ch_id].dict_cities)))

        if message.content == "Игра":
            if all_user_list[ch_id].game_session:
                await message.channel.send("Вы уже играете!")
            else:
                all_user_list[ch_id].game_session = True
                await message.channel.send(first_start_game(all_user_list[ch_id].dict_cities))

