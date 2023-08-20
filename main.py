from random import choice, randint, uniform

vowels = 'ayuioa'
consonants = 'qwrtrtpsdfghjxcvbnm'

#функция генерации псевдоимен
def psevdo_name_gen():
    rword = ''
    for _ in range(randint(4, 7)):
        rword += choice(vowels + consonants)
    return rword.capitalize()

# функция записи в файл
def add_word(word: str, count_words: int):
    with open(word, 'w') as names_file:
        for _ in range(count_words):
            names_file.write(psevdo_name_gen() + '\n')


def file_numbers(name, count_str):
    with open(name, 'w') as f:
        for _ in range(count_str):
            f.write(f'{randint(-1000, 1000)} | {uniform(-1000, 1000)}\n')

if __name__ == '__main__':
    add_word('names.txt', 3)
    file_numbers('number.txt', 6)