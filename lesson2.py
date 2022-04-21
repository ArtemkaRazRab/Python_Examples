# Запись данных

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors) # разделителей не будет
# data.close()

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close()

# Файлы можно записывать ешё вот так

# with open('file.txt', 'a') as data:
#     data.write('line 111\n')
#     data.write('line 222\n')


# Чтение данных

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()


# Функции и модули

# import lesson1
# print(lesson1.f(1))

# Можно записывать вот так

# import lesson1 as l1
# print(l1.f(2.3))


# def new_string(symbol, count):
#     return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # TypeError missing 1 req

# def new_string(symbol, count = 3):
#     return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!!
# print(new_string(4)) # 12


# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2
# # print(conatenatio(1, 2, 3, 4)) # TypeError: ...

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2) # для n=3 берем данные из (n=2) + (n=1)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34

# a = (3, 1, 41, 4)
# print(a)
# print(a[-2])

# a = (3, 1, 41, 4)
# for item in a:
#     print(item)


# Словари

# dictionary = {}
# dictionary = \
# {
#     'up': '↑',
#     'left': '←',
#     'down': '↓',
#     'right': '→'
# }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←

# dictionary = {}
# dictionary = \
# {
#     'up': '↑',
#     'left': '←',
#     'down': '↓',
#     'right': '→'
# }
# for k in dictionary.keys():
#     print(k)


# Множества

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}