# Вспоминаем задачу 3 из прошлого семинара.
# Мы сформировали текстовый файл с псевдо именами
#  и произведением чисел.
#  Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
#  Имена пишите с большой буквы.
#  Каждую пару сохраняйте с новой строки.

import json

with open('result.txt', 'r') as f:
    data = f.read().split('\n')[:-1]
    #print(data)
res_list = []
for note in data:
    name, mult = note.split()
    res_list.append({'name': name, 'muit': float(mult)})
#print(res_list)

with open('result.json', 'w') as f_json:
    json.dump(res_list, f_json, indent=4)

    
