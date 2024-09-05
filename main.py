#   - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
my_dict = {'Alex' : 1998, 'Bob' : 2000, 'Tom' : 1989, 'Anna' : 2001, 'Luisa' : 1980 }

#   - Выведите на экран словарь my_dict.
print('Dict: ', my_dict)

#   - Выведите на экран одно значение по существующему ключу,
#   одно по отсутствующему из словаря my_dict без ошибки.
print('Existing key = "Bob": ',my_dict['Bob'])
print('Not existing key "Oleg": ',my_dict.get('Oleg'))
print('Not existing key "Oleg": ', my_dict.get('Oleg', 'Такой ключ не найден'))

#   - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
my_dict['Oleg'] = 2003
my_dict.update({'Simona' : 2000, 'Max' : 2002})

#  - Удалите одну из пар в словаре по существующему ключу из словаря my_dict
#  и выведите значение из этой пары на экран.
print('Deleted value: ', my_dict.pop("Luisa"))

#   - Выведите на экран словарь my_dict.
print('Modified dictionary: ', my_dict)

print('-' * 70)

#   - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных
#   с повторяющимися значениями.
my_set = {'Cat', 'Dog', 10, 25, 'Cat', 'Cat', 10, 10, True, True, 25, ('Green', 'Blue', 'Red')}

#   - Выведите на экран множество my_set (должны отобразиться только уникальные значения)
print('Set: ', my_set)

#   - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
my_set.add(14)
my_set.add('Bird')

#   - Удалите один любой элемент из множества my_set.
my_set.discard('Cat')

#   - Выведите на экран измененное множество my_set.
print('Modified set: ', my_set)
