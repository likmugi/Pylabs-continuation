# Множества - Set or Frozenset
# Для определения множеств использутся фигурные скобки, в которых перечисляются элементы.

f_set = {1, 2, 3, "Alex", "John", 3}
print(f_set) # множества содержат только уникальные значения

# еще один вариант определения множества (в функцию можно помещать список или кортеж)
# + удобна если нужно пустое множество
n_set = set(["Greg"])

f_set.add("Lika")
print(f_set)

# удаляем элемент при помощи метода remove, в который передаем элемент;

f_set.remove("Alex")

# следует проверять на наличие элементов в множестве, т.к. есть вероятность выпада ошибки
user = "Lika"
# так, если у нас значение переменной будет входить в множество, то удаляем из множества значение
# если такого элемента не будет в множестве, то все просто останется на месте
if user in f_set:
    f_set.remove(user)
print(f_set)

# есть еще метод discard, который не будет генерировать ошибку, даже если такого значения не будет в множесте
f_set.discard(5)
print(f_set)

# для перебора множестd очень удобно использовать цикл for
for users in f_set:
    print(users)

# проверить наличие значения в множестве можно так
print("Alex" in f_set)

# С помощью метода copy можно скопировать содержимое оного множества в другое
s_set = f_set.copy()
print(s_set)
sn_set = {"Dima", "Nikita", "Anton", "John"}
t_set = f_set.union(sn_set)
print(t_set)

# пересечение множеств позволяет получить только те элементы, которые есть в обоих множествах
t_set = f_set.intersection(sn_set)
print(t_set)

# разность множеств: получение элементов, которые есть в set1, но отсутвуют в set2
tn_set = f_set.difference(sn_set)
print(tn_set)

# можно реализовать иначе
print(f_set - sn_set)

# если говорить об отношениях множеств, то можно выяснить является ли одно подмножеством другого
print(t_set.issubset(f_set))

print('\n')

# Словари - структура данных, позволяет хранить объекты, для доступа к которым используется ключ
# называют еще "ассоциативный массив"; предназначена для хранения объектов с доступом по ключу.

# пустой словарь можно создать, указав фигурные скобки или используя функцию dict
dct = {}
dct2 = dict()
# print(type(dct), type(dct2))

age = {"John":27, "Alex":35, "Ben":42}
print(age)

# чтобы добавить элемент в словарь, нужно указать новый ключ и его значение
age["Dima"] = 19
print(age)

# как видно, в качестве ключей используются строки, а в качестве значений - числа,
# т.е. они необязательно должны быть однотипными

# для удаления элемента из словаря можно воспользоваться командой del
del age["John"]
print(age)

# доступ к элементам словаря осуществляется так же как и к элементам списка,
# только в качестве индекса указывается ключ
print(age["Alex"])

# можно проверить наличие на ключ в словаре (при помощи оператора in)
print("Ben" in age)
print("John" in age)

# методы словарей
age2 = age.copy() # создает новую копию словаря
print(age.get("Ben")) # возвращает значение из словаря по ключу
print(age.items()) # возвращает элементы словаря по ключу и значению в отформатированном виде
print(age.keys()) # возвращает ключи словаря
print(age2.pop("Ben")) # если указанный ключ есть в словаре, то данный элемент удалиться из словаря и возвратиться значение
print(age2)
print(age2.popitem()) # удалит последний элемент и вернет пару ключ-значение из словаря
print(age2.values()) # возвращает значение элементов словаря
age3 = {"Alex":23, 3:12, "Ben-ben":30}
age3.update(age) # используется, чтобы обновить значения из одного словаря при помощи другого
print(age3)
age.clear() # удаляет все элементы словаря

# для перебора элементов используем цикл for
for key in age3:
    print(key, " - ", age3[key])

# есть еще один способ перебора элементов
for key, value in age3.items():
    print(key, " -- ", value)

# Генераторы
