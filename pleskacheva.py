#Плескачёва Таисия Вариант 3 ИСУ 502603
from csv import reader
import random
import xml.dom.minidom as minidom


def Zadanie_1():
    with open('books.csv') as file:
        table =list(reader(file, delimiter=';'))
        count_30, cont_year_book = 0, 0
        for row in table:
            if len(row[1]) > 30:
                year_book = int(str(row[6].split()[0]).split('.')[2])
                if year_book == 2014 or year_book == 2016 or year_book == 2017:
                    cont_year_book += 1
                count_30 += 1
        print(f'Количество книг, у которых в названии больше 30 символов: {count_30}, и которые при этом 2014, 2016 или 2017 года: {cont_year_book}')


def Zadanie_2():
        while True:
            years = [2014, 2016, 2017]
            flag = 0
            search = input('Введите автора: ')
            if search == '0':
                break
            with open('books.csv', 'r') as file:
                table = list(reader(file, delimiter=';'))
                for row in table[1:]:
                    lower_case = row[4].lower()
                    index = lower_case.find(search.lower())
                    year_book = int(str(row[6].split()[0]).split('.')[2])
                    if index != -1 and year_book in years:
                        print(f'{row[1]} , {row[4]}')
                        flag += 1
                if flag == 0:
                    print('Ничего не найдено.')
                    break
                else:
                    print(f'Найдено {flag} книг.')


def Zadanie_3():
    with open('books.csv', 'r') as file:
        table = list(reader(file, delimiter=';'))
        with open('output.txt', 'w') as output:
            for i in range(20):
                row = table[random.randint(1,len(table))]
                year = int(str(row[6].split()[0]).split('.')[2])
                output.write(f'{i+1}. Автор: {row[4]}. Название: {row[1]}. Год: {year}.\n')


def Zadanie_4():
    xml_file = open('currency.xml', 'r', encoding='windows-1251')
    xml_data = xml_file.read()
    dom = minidom.parseString(xml_data) # Создаём DOM-дерево из строки XML
    dom.normalize() # Нормализуем DOM-структуру
    elements = dom.getElementsByTagName('Valute') # Получаем список всех элементов <Valute>
    names_list = []
    for node in elements: # Перебираем каждую валюту
        for child in node.childNodes: # Перебираем все дочерние узлы валюты
            if child.nodeType == 1: # Проверяем, что узел — элемент
                if child.tagName == 'Nominal': # Если тег <Nominal>
                    if child.firstChild.nodeType == 3: # Проверяем, что является текстом
                        nominal = child.firstChild.data # Получаем номинал валюты
                if child.tagName == 'Name': # Если тег <Name>
                    if child.firstChild.nodeType == 3:# Проверяем, что является текстом
                        name = child.firstChild.data # Получаем название валюты
        if nominal == '1':
            names_list.append(name)
    print(names_list)
    xml_file.close()


def matrix_index(string, matrix): # Функция для определения номера подмассива в двухмерном массиве
    for i, row in enumerate(matrix):
        if string in row: 
            return i

def Dop_Zadanie(): #Выводит теги без повторений, выводит 20 самых популярных книг, создаёт текстовый документ, в которм прописывает тег (ID), название книги и количество выдач
    with open('books.csv') as file:
        table =list(reader(file, delimiter=';'))
        with open('out.txt', 'w') as out: 
            element = []
            print('Все теги без повторений: ', end = '')
            for row in table[1:]:
                if any(sub[0] == row[0] for sub in element):
                    element[matrix_index(row[0], element)][2] += int(row[8])
                else: 
                    element.append([row[0], row[1], int(row[8])])
            for i in range(len(element)):
                    out.write(f"{i + 1}. {element[i][0]}; {element[i][1]}; {element[i][2]}\n")
                    print(element[i][0], end='')
                    if i != len(element) - 1:
                        print(', ', end=' ')
            print()
        element.sort(key = lambda x: x[2], reverse=True)
        print('Вот 20 самых популярных книг: ')
        for i in range(20):
            print(f'{i + 1}. {element[i][1]}')


Zadanie_1()
Zadanie_2()
Zadanie_3()
Dop_Zadanie()