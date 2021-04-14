cities = dict()
city_key = ''

def dict_cities():
    """
    Функция возвращет словарь городов с ключом по
    по первой букве
    :return: словарь городов
    """

    with open('CITIES.md', 'r', encoding='Windows-1251') as file:
        for line in file:
            cities[line[0].lower()] = line[:-1]
    return cities

def game_city(client_message_city):
    """
    Функция ищет в словаре cities города по ключу
    из сообщения клиента
    :param client_message_city: работа с str
    :return: строковое значение города или
    сообщение о победе
    """
    city_key = (client_message_city[-1] if not
                client_message_city[-1] in ['ь', 'ы'] else
                client_message_city[-2])

    if cities.get(city_key) == None:
        return f'Вы выйграли я незнаю больше городов'
    return cities.pop(city_key)
