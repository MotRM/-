from collections import defaultdict
from dataclasses import dataclass, field
import types

all_user_list = defaultdict(list)

@dataclass
class CityGameSession():
    """Тип данных чат"""
    chat_id: int = None
    user_id: int = None
    game_session: bool = None
    dict_cities: defaultdict(list) = field(init=False)

    def __post_init__(self):
        # инициализация переменной dict_cities
        self.dict_cities = defaultdict(list)

        with open('C:/Users/motr8/Desktop/Projects/Core/CITIES.md', 'r', encoding='Windows-1251') as file:
            for line in file:
                self.dict_cities[line[0].lower()].append(line[:-1])



