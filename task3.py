# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

from main import file_numbers, add_word
from typing import TextIO

# функция, которая читает строки и при окончании возвращается в начало
def read_file(file: TextIO) -> str:
    text = file.readline()
    if not text:
        file.seek(0)
        text = file.readline()
    return text[:-1]

# функция, которая будет считывать информацию из двух файлов и их обрабатывать
def creat_mult(file_names: str, file_numbers, file_res):
    with (open(file_names, 'r') as f_names,
          open(file_numbers, 'r') as f_nums,
          open(file_res, 'w') as f_res):
        #print(f_names.read(), f_nums.read())

        # if len(f_names.read().split('\n')) > len(f_nums.read().split('\n')):
        #     max_file_len = len(f_names.read().split('\n'))
        # else:
        #     max_file_len = len(f_nums.read().split('\n'))

        len_names = len(f_names.readlines())
        len_nums = len(f_nums.readlines())
        max_file_len = max(len_names, len_nums)
       
       
        #print(f_names.read())

        
        for _ in range(max_file_len):
            num1, num2 = map(float, read_file(f_nums).split('|'))
                       
            names = read_file(f_names)
            mult = num1 * num2
            print(names, mult)
            
            if mult < 0:
                f_res.write(f'{names.lower()} {abs(mult)}\n')
            else:
                f_res.write(f'{names.upper()} {int(mult)}\n')


if __name__ == '__main__':
    word_name = 'word_list.txt'
    num_name = 'num_list.txt'
    

    file_numbers(num_name, 5)
    add_word(word_name, 10)
    creat_mult(word_name, num_name, 'result.txt')
