import random
from collections import defaultdict

cities = defaultdict(list)
city_key_bot = ''
city_key_client = ''
first_city = ''
first_city_key = ''

with open('CITIES.md', 'r', encoding='Windows-1251') as file:
    for line in file:
        cities[line[0].lower()].append(line[:-1])

def first_start_game():

    """ Данная функция запускается при
    вводе команды и определяет кто называет
     город первым. """

    if random.randint(0, 5) > 2:
        return f'Вы называете город первым!'
    else:
        random_values_city = random.choice(list(cities.values()))
        first_city = random_values_city[random.randint(0, len(random_values_city) - 1)]
        first_city_key = first_city[0].lower()
        cities[first_city_key].remove(first_city)
        return f'Я хожу первым!\nГород: {first_city}'
print(first_start_game())