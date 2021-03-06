#   Rортеж в Python это:

# последовательность элементов, которые разделены между собой запятой и заключены в скобки
# неизменяемый упорядоченный тип данных
# Грубо говоря, кортеж - это список, который нельзя изменить. То есть, в кортеже есть только права на чтение. Это может быть защитой от случайных изменений.


# Создать пустой кортеж:
tuple1 = tuple()

# кортеж из списка 
list_keys = ['hostname', 'location', 'vendor', 'model', 'ios', 'ip']

tuple_keys = tuple(list_keys)

# К объектам в кортеже можно обращаться, как и к объектам списка, по порядковому номеру:
print(tuple_keys[0])
# !!! Но так как кортеж неизменяем, присвоить новое значение нельзя:


# Функция sorted сортирует элементы кортежа по возрастанию и возвращает новый список с отсортированными элементами
sorted(tuple_keys)