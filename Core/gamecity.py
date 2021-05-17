import random

city_key_bot = ''
city_key_client = ''
first_city = ''
first_city_key = ''

def first_start_game(dict_cities):

    """ Данная функция запускается при
    вводе команды и определяет кто называет
     город первым. """

    if random.randint(0, 5) > 2:
        return f'Вы называете город первым!\n' \
               f'Чтобы закончить наберите Закончить'
    else:
        random_values_city = random.choice(list(dict_cities.values()))
        first_city = random_values_city[random.randint(0, len(random_values_city) - 1)]
        first_city_key = first_city[0].lower()
        dict_cities[first_city_key].remove(first_city)
        return f'Я хожу первым!\nГород: {first_city}\nЧтобы закончить наберите Закончить'

def game_city(client_message_city, dict_cities):
    """
    Функция ищет в словаре cities города по ключу
    :param client_message_city: работа с str
    :return: строковое значение города или
    сообщение о победе
    """
    city_key_bot = (client_message_city[-1] if not
                client_message_city[-1] in ['ь', 'ы'] else
                client_message_city[-2])

    try:
        city_key_client = client_message_city[0].lower()
        dict_cities[city_key_client].remove(client_message_city)
    except ValueError:
        return f'Вы ввели город не правильно или такой город уже был'

    if dict_cities.get(city_key_bot) == None:
        return f'Вы выйграли! Я незнаю больше городов!'

    city_result = dict_cities.get(city_key_bot)[0]
    dict_cities[city_key_bot].remove(city_result)

    return city_result

def clear_dict_cities(dict_cities):
    dict_cities.clear()
    with open('C:/Users/motr8/Desktop/Projects/Core/CITIES.md', 'r', encoding='Windows-1251') as file:
        for line in file:
            dict_cities[line[0].lower()].append(line[:-1])

