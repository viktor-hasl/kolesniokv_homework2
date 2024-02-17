# Viktor Kolesnikov
# Date: 13/02/2024
# Description: Homework 2
# Grodno IT Academy Python 3.11

# Объяснение работы с функциями:
# формат определения функции (то есть: мы ее создаем) - def func(arg1, arg2, arg3)
# arg1, arg2, arg3 - это аргументы, которые передаются в функцию при ее вызове (то есть, мы ее запускаем)

# Оценивается: чистота кода, наличие комментариев (PEP8), прохождение всех тестов
# нельзя менять названия функций/файлов/входные данные. Можно менять решение, менять/добавлять return.

# пример названия репозитория для гитхаба: kazukevich_homework2
# добавьте в репозиторий с домашним задание файл readme.md с датой сдачи, фамилией и именем выполнившего и кратким
# описанием каждой задачи (коротко, что использовали, алгоритм функции), оформленным в стиле markdown


# Напишите программу, которая считает общую цену.
# Вводится m рублей и n копеек цена, а также количество s товара.
# Посчитайте общую цену в рублях и копейках за l товаров.
# Уточнение:
# Используйте функцию return чтобы ответ был в рублях и копейках.
# Ответ должен быть в формате: "Общая цена составляет M рублей и N копеек за L товаров"

# * Для одного из тестов нужно применять какую-то библиотеку =)


# Данну библиотеку мы ипортируем для точной работы с числами с плавающей точкой
from decimal import Decimal
# Требуется для того, чтобы можно было перевести строку во множество без потери порядка символов
from collections import OrderedDict
import re


def common_price(m, n, s, l):
    """Пишем функцию, которая принимаем значения:
    m - Количество рублей за товары s
    n - Количество копеек за товары s
    s - Количество товаров за сумму m рублей n копеек
    l - Количество товара, которым нужно рассчитать цену зная какая будет цена за s товаров
    """
    # Проверяем значения ввода на наличие другого типа данных
    if m != int(m) or n != int(n) or s != int(s) or l != int(l):
        return False
    elif s <= 0 or (m <= 0 and n <= 0) or l < 0:  # Проверяем значения на их корректность
        return False
    else:
        # Используя пропорцию считаем сколько будет цена за l товара, используя Decimal для более точной работы
        # с числами. Рубли и копейки даны в целых числах поэтому мы копейки переводим в сотые и складываем с рублями
        # и получаем цену за s товаров
        summa = (Decimal(m) + Decimal(n) / 100) * Decimal(l) / Decimal(s)
        a = int(summa)  # Убираем значения после точки и получаем рубли
        v = ((summa - a) * 100).quantize(Decimal(1))  # Вычитаем рубли, получаем копейки, а затем округляем до целого
        d = l  # Количество товаров


    return "Общая цена составляет " + str(a) + " рублей и " + str(v) + " копеек за " + str(d) + " товаров"



# Даны: три стороны треугольника.
# Требуется: проверить, действительно ли это стороны треугольника.
# Если стороны определяют треугольник, найти его площадь с точностью до четырёх десятичных.
# Пример: если строны треугольника равны 2, 2, 2 то мы должны вернуть 1.7321
# Если нет, вывести False.
# Бонусом - с правильным возвратом мы ещё получим обьяснение в консоль почему это не треугольник.


def triangle(a, b, c):
    """Даны три стороны треугольника, в начале мы проверим являются ли числа треугольником,
    зная что сумма двух сторон не должна быть меньше либо ровна третей стороне, выяснив что стороны
    являются треугольником мы считаем и выводим площадь треугольника по формуле Герона
    """
    # Проверяем на корректность
    if a == str(a):
        print(f'Ошибка, значений {a} является строкой')
        return False
    elif b == str(b):
        print(f'Ошибка, значений {b} является строкой')
        return False
    elif c == str(c):
        print(f'Ошибка, значений {c} является строкой')
        return False

    # if a >= b + c or b >= a + c or c >= a + b:
    if a >= b + c:
        print(f"По данным можно сказать, что стороны не являются треугольником, так как при сложении сторон, сторона: {a},"
              f" больше либо ровна сумме: {b + c} других сторон")
        return False
    elif b >= a + c:
        print(f"По данным можно сказать, что стороны не являются треугольником, так как при сложении сторон, сторона: {b},"
              f" больше либо ровна сумме: {a + c} других сторон")
        return False
    elif c >= a + b:
        print(f"По данным можно сказать, что стороны не являются треугольником, так как при сложении сторон, сторона: {c},"
              f" больше либо ровна сумме: {b + a} других сторон")
        return False
    else:
        # Находим полупериметр, затем и площадь треугольника
        p = (a + b + c)/2
        s = (p * ((p - a) * (p - b) * (p - c))) ** 0.5
        return round(s, 4)


# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении могут быть знаки препинания.
# Пример: если введено "This is a sample sentence where the longest word is in the middle!",
# то надо вернуть "sentence"
def longest_word(sentence):
    """Принимая предложение мы с помощью регулярных выражений удаляем все знаки препинания
    и разделяя слова по пробелу переводим в список, а затем через цикл ищем самое длинное слово,
    если слова равны, то мы берем последнее
    """
    if sentence != str(sentence) or len(sentence) == 0:
        return False
    else:
        sentence = re.sub(r'[.,!:;?"\']', '', sentence).split()
        long_word = ''
        for i in sentence:
            if len(i) >= len(long_word):
                long_word = i
        return long_word


# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".
def uniques(repeating_string):
    """Принимаем строку, убираем все пробелы с помощью replace,
    затем с помощью OrderedDict.fromkeys() переводим во множество
    тем самым избавляясь от повторяющихся символов
    """
    # Проверяем на корректность данные
    if repeating_string != str(repeating_string):
        return False
    else:
        set_ = OrderedDict.fromkeys(repeating_string.replace(' ', ''))
        # C помощью join() склеиваем множество из символов
        return ''.join(set_)


# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Проверка рассчитана только на английские буквы.
def count_string_capitalization(mixed_string):
    """Используя регулярные выражения можно легко решить данную задача,
    с помощью re.findall мы находим все заглавные и считаем их количества,
    аналогично для прописных
    """
    if type('string') != type(mixed_string):
        return False
    else:
        letters_upper = len(re.findall(r'[A-Z]', mixed_string))
        letters_lower = len(re.findall(r'[a-z]', mixed_string))
        return f"В строке '{mixed_string}' {letters_upper} большие и {letters_lower} маленькие буквы"
