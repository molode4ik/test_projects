# Number 1
string_of_odd_numbers = (str(number) for number in range(1,101) if number % 2 != 0)
print("".join(string_of_odd_numbers))
# Number 2
b = 10


# def f(a):
#     print(a)
#     print(b)
#     b = 15
#
#
# f(3)
# Функция не знает переменную b так как мы не передаем ее в функцию, чтобы можно было работать с переменной b нужно либо
# создавать класс либо делать b глобальной(не желательно)
# Number 3
# t = (1, 2, [50, 60])
# t[2] += [10, 20]
# Кортежи в Python являются неизменяемыми объектами а мы в 19 строчке обращаемся к элементу кортежа и пытаемся изменить его


# Number 4
def reverse_word(word: str) -> str:
    return word[::-1]


def is_palindrome(word: str) -> bool:
    return True if word == word[::-1] else False


word = "Analog"
reverse_word = reverse_word(word)
is_palindrome = is_palindrome(reverse_word)
print(reverse_word, is_palindrome)


# Number 5
def count_words_in_each_line(file):
    try:
        with open(file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for index, line in enumerate(lines):
                line = line.strip()
                words = line.split()
                print(f"Строка {index + 1}: {len(words)} слов(а)")
    except FileNotFoundError:
        print(f"Файл '{file}' не найден")


file_path = '../Number5.txt'
count_words_in_each_line(file_path)
