from collections import defaultdict
from dataclasses import dataclass, field
import types
# словарь с обьектами класса CityGameSession
all_user_list = defaultdict(list)

@dataclass
class CityGameSession():

    """
    Класс создает объект с атрибутами:
    chat_id: int - ID чата
    user_id: int - ID пользователя
    game_session: bool - показывает запущена ли игра,
    при True игра запущена
    dict_cities: defaultdict - словарь с городами
    """

    chat_id: int = None
    user_id: int = None
    game_session: bool = None
    dict_cities: defaultdict(list) = field(init=False)

    def __post_init__(self):

        """
        Инициализация атрибута
        dict_cities (словаря с городами)
        """

        self.dict_cities = defaultdict(list)

        with open('C:/Users/motr8/Desktop/Projects/Core/CITIES.md', 'r', encoding='Windows-1251') as file:
            for line in file:
                self.dict_cities[line[0].lower()].append(line[:-1])



