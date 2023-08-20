# Напишите функцию, которая сереализует содержимое
# текущей директории в json-файл.
# В файле должен храниться список словарей, словарь
# описывает элемент внутри директории: имя, расширение, тип.
# Если элемент - директория, то только тип и имя. 
# Пример результата для папки, где лежит файл test.txt и директория directory_test:
# [
# {
# 'name': 'test',
# 'extension': '.txt',
# 'type': 'file'
# },
# {
# 'name': 'directory_test',
# 'type': 'directory',
# }
# ]

import json
import os
from pathlib import Path


# print(os.listdir())
# list_d = os.listdir()
# print(list_d)


list_dict_dir = []

with open('list_dict_dir.json', 'w') as l_d_d:
    for dir_path, dir_name, file_name in os.walk(os.getcwd()):
        for name_dir in dir_name:

            list_dict_dir.append({'name': name_dir,
                               'type': 'directory'})
        for name_file in file_name:
            name, ext = name_file.split('.', 1)
            list_dict_dir.append({'name': name,
                               'extension': ('.' + ext),
                               'type': 'file'})
    
    json.dump(list_dict_dir, l_d_d, indent=4)


# list_dict_dir = []
# with open('list_dict_dir.json', 'w') as l_d_d:
#     for note in list_d:
#         name, ext = note.split('.', 1)
#         list_dict_dir.append({'name': name,
#                                'extension': ('.' + ext),
#                                'type': 'file'})
    
#     json.dump(list_dict_dir, l_d_d, indent=4)    


