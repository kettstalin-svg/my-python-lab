# year = '2026'

# year = int(year) # int - Число и переделывает другой ввид в int


# print(year * 10)

# print(type(year))



# # Числа и спомобы примера использования.
# print(2 ** 3)
# print( 10 // 3) # Многочисленное деление


# print(10 % 3) # сКОЛЬКО ОСТАЛОСЬ


# num1 = 8
# num2 = 9



# print(num1 % 2)
# print('Четное:', num2 % 2)
# print(round(3.14)) # round - Округление числа int.


# часть 2 true false


# print(bool(0)) # bool - проверка истинны
# print(bool(1))
# print(bool(''))
# print(bool('hi'))

# b = True

# print(type(b))

# scorre = None # None - Нечего
# print(bool(scorre))

# Конец, практика.

# 1 Задание: End.
# work = 'ha'

# z = work * 7
 
# print(z)


# 2 Задание: End.
# a = 17
# b = 4

# print(a / b) ; print(a // b) ; print(a % b) ; print(a == b)


# # 3 Задание:  End?
# x = int('2026')
# x = float(x)
# y = '17.77'
# y = float(y)
# print(type(x))
# print(type(y))

# # 4 Задание End.
# total = 100
# bonus = 50
# print('Total:', total + bonus)

# 5 Задание: End.

# price = '12a'
# price = int(price)
# print(price)
# print('ValueError', 'Потому что в строке 12а присутствует буква которая является типом данных str')


# # 6 Задание:

# print(bool(0)) # 0 не являеться истиной.
# print(bool(1)) # 1 являеться истинной.
# print(bool(0.0)) 
# print(bool(''))
# print(bool('0'))
# print(bool(None))


# Progrmatic = input('Какой язык програмирования вы изучаете? ')
# if Progrmatic == 'Python':
#     print('Молодец')
# else:
#     Progrmatic != 'Python'
#     print('Ну ты и какашка')  


# lange = 'Python'


# age = 20

# print(lange == 'pY' or age >= 20)  # or - если хоть одно действие выполниться то выводит истинну

# if age < 10:
#     print('Дост3уп запрещен')
# elif age > 18 and  99:
#     ('Доступ разрешен')
# elif age >= 99:
#     print('Ты очень старый для технологий')


# num = int(input('Введи число: '))


# if num % 2 == 0:
#     print('Четное')
# else:
#     print('нечетное')


# for i in range(1, 5000, 9999999999999999): # range - Повторяет строку сколько написано в скобках.
#     text = 'hi'
#     print(i, text)

# count = 0
# while count < 5:   # while - Выполняет код до какого-то момента.
#     print('hi')
#     count += 1


# result = 0

# for i in range(4):
#     num = int(input())
#     if num < 0:
#         continue      # break -прерывает цикл при определенных условиях.
#     result += num     # continue - пропускает конкретную итерацию.

# print('Сумма всех введеных чисел: ', result)

# # Задания: ВернутьсЯ позже!
# for i in range(3, 3, 4):
#     print(i, num)

# name = 'PERSONA'
# print('P' in name)


# phone_num = '896777390114'
# print(phone_num[0])
# print(phone_num[19])

# phone_num = '89677739013'
# lange = 'Python'
# print(phone_num[1:4])
# print(lange[3:4])

# city = 'alabuga'

# len(city)     # len - Возращает количество элементов объекта.

# pri
# print(city.capitalize())  # capitalize - Ставит в начале строки заглавную букву.

# city = 'llll'

# print(len(range(5)))

# city = 'MoscOw'

# print(city.capitalize())

# print(city.lower())  # lower - Функция которая заменяет все заглавные буквы на маленькие.
# print(city.upper())  # upper - Функция позволящеяся все буквы в строке заглавными.


# phone_num = '+79677739013'
# phone_num = phone_num.strip()  # strip - нужен для удаления пробелов.
# if phone_num.startswith('+7'):  # staetswith - проверяет есть ли то что прописано в начале строки.
#       print('Российский номер')
# else:
#       print('Неизвестным номер')                     

# print(phone_num.endswith('777.')) # endswith - Нужен для проверки конца строки.

# print(phone_num.replace('+7'), '8'))  # replace - Заменяет старый на новый.

# print(phone_num.count('7')) # count - Считает сколько символов в строке.

# print('hi')

# # Списки:
# l = ['stroka1', 15, 5.2, 'stroka2']
# print(l)
# # print(type(l[0]))  # Строки имеют класс list
# print(len(l))
# print(15 in l)

# new_list = []
# print(new_list)

# print(list(range(5)))

# my_list = [9, 100, 0.6, 1, 3,5]

# print(sum(my_list))  # sum - складывает все числа в одно.
# print(min(my_list))  # min - выводит минимальное число.
# print(max(my_list))  # max - Выводит максимальное число.
# my_list = [2, 5, 99]
# my_list.append('PYTHON')  # append - добавляет в список что есть в строке.

# print(my_list)

# my_list.insert(0, 1)
# print(my_list)

# #Удаление:
# delete = my_list.pop(0) # pop - Удаляет определенную строку под  индексом.

# print(f"my_list: {my_list} | Deleted: {delete}")

# my_list.remove(99)
# print(my_list)

# print(my_list.sort(reverse=True))


# numbers = [0, 1, 2, 3, 4, 5 ,6]
# for i in numbers:
#     print(i)

# lange = ['Py', 'JS', 'C++']

# for index, element in enumerate(lange): # enumerate -  Также возращает индекс.
#     print(index, el)

# string = 'Я будущий Python разработчик' # split - разделяет слова на список.
# my_list = print(string.split())
# print(my_list)

# ip = '127.0.01'
# print(ip.split())

# my_list = ['Я', 'будущий', 'Python', 'Разработчик']


# numbers = [12, 5, 8, 99, 3, 8]

# avtor = {
#     'name': 'Gondon',
#     'age': 16,
    
# }

# print(avtor['name'])
# print(avtor.get('surname', 'Gongin')) # get - добавить элемент.

# avtor['age'] = 19
# avtor['porvalsa'] = True
# avtor.pop('name')

# print(avtor)

# avtor = {
#     'name': 'MAMA TVOR',
#     'age': 16,
#     'VUEBANA': True,
# }


# user = ['MAMA TVOR', 26,    True]

# for pair in avtor.keys():
#     print(pair)
# print(f'Ключи: {avtor.keys()}')

# for pair in avtor.values(): # values - для вывода значений
#     print(pair)

# print(f'Значения: {avtor.values()}')


# for  key, value in avtor.items():  # ITEMS - ДЕЛАЕТ КЛЮЧЗНАЧЕНИЕ
#     print(f'Ключ: {key}, Значение: {value}')
info = {'name': 'Ale', 'surname': 'mak'}

info['name']= 'Kirill'

print('info')