# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
#  После каждого ввода добавляйте новую информацию в
# JSON файл.
#  Пользователи группируются по уровню доступа.
#  Идентификатор пользователя выступает ключём для имени.
#  Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
#  При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json

# data = {
#   1: [{"id": 1234,
#      "name": "John"},
#      {"id": 2222,
#      "name": "Max"}],
#   2: [],
# }


# while True:
#     name = input('Введите имя:  ')
#     id = int(input('Введите id: '))
#     level = int(input('Введите уровень доступа: '))


#     temp = data.get(level, [])
#     temp.append({'id': id, 'name': name})
#     data[level] = temp
#     print(data)

def apdate_data(data):
    name = input('Введите имя:  ')
    id = int(input('Введите id: '))
    level = input('Введите уровень доступа: ')

    temp = data.get(level, [])
    temp.append({'id': id, 'name': name})
    data[level] = temp
    
    return data

# data = {
#   1: [{"id": 1234,
#      "name": "John"},
#      {"id": 2222,
#      "name": "Max"}],
#   2: [],
# }

def data_base_control(file_name: str = 'data_base.json'):
    while True:
        try:
            with open(file_name, 'r') as f_j:
                data = json.load(f_j)
        except FileNotFoundError:
            data = {}
        
        data = apdate_data(data)

        with open(file_name, 'w') as f_j:
            data = json.dump(data, f_j, indent=4)

if __name__ == '__main__':
    data_base_control('new_file.json')
