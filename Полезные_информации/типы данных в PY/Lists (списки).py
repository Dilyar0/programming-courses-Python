#                                       list(список в py) это то же самое что массивы

list = [1,2,3,4,5,6]

# элементы из массива можно достать через индекс
print(list[1]) #2

# Перевернуть список наоборот можно с помощью метода reverse():
list.reverse()

# Функция len возвращает количество элементов в списке
len(list)

# функция sorted сортирует элементы списка по возрастанию и возвращает новый список с отсортированными элементами
names = ["john", "Aman", "Sarah", "Atosh"]

sorted(names)

print(names)

#----------------------------------------методы листа


#Метод append добавляет в конец списка указанный элемент
vlans = ['10', '20', '30', '100-200']
vlans.append('300')


# Если нужно объединить два списка, то можно использовать два способа: метод extend и операцию сложения
vlans2 = ['300', '400', '500']
vlans.extend(vlans2)


# Метод pop удаляет элемент, который соответствует указанному номеру. Но, что важно, при этом метод возвращает этот элемент
vlans.pop(-1) # '100-200'
# Без указания номера удаляется последний элемент списка.


#Метод remove удаляет указанный элемент
vlans.remove()

# Метод index используется для того, чтобы проверить, под каким номером в списке хранится элемент:
vlans.index()

# Метод insert позволяет вставить элемент на определенное место в списке:
vlans.insert(1, '15') # в 1 индекс листа всатится 15

# Метод sort сортирует список на месте:
vlans.sort()
