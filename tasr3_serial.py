# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
#  Дополните id до 10 цифр незначащими нулями.
#  В именах первую букву сделайте прописной.
#  Добавьте поле хеш на основе имени и идентификатора.
#  Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
#  Имя исходного и конечного файлов передавайте как аргументы
# функции.

import json
import csv

with open('data_base.json', 'r') as f_j:
    data = json.load(f_j)

res_list = []
for key, values in data.items():
    for i in values:
        res_list.append({'level': key,
                         'id': i['id'],
                          'name': i['name']
                          })

# with open('res_data_base.csv', 'w') as f_csv:
#     temp = csv.DictWriter(f_csv,
#                           fieldnames=['level', 'id', 'name'],
#                           delimiter= ";")
#     temp.writeheader()
#     temp.writerows(res_list)

with open('res_data_base.csv', 'w') as f_csv:
    for user in res_list:
        f_csv.write(f'{user["level"]}, {user["id"]}, {user["name"]}\n')
