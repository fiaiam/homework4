my_string = input('Введите любую фразу: ')
print('Количество символов введённого текста ','"', my_string,'"', 'составляет: ', len(my_string))
#Выведите строку my_string в верхнем регистре.
print(my_string.upper())
#Выведите строку my_string в нижнем регистре.
print(my_string.upper().lower())
#Измените строку my_string, удалив все пробелы.
print(my_string.replace(' ', ''))
#Выведите первый символ строки my_string.
print(my_string[0])
#Выведите последний символ строки my_string.
print(my_string[-1])