print('Разбираем функцию «map»')


# def f(x):
#     return x ** 2
#
#
# l = [1, -5, -6]
# print('Возводим в квадрат все элементы')
# print(list(map(f, l)))
#
# print('Функция «abs» делает все элементы положительными, убирает предшествующий знак минус')
# print(list(map(abs, l)))
#
# print('Это то же самое, но при помощи генератора списков')
# print([abs(i) for i in l])
#
# c = ['list', 'two', 'true']
# print('Получаем длину каждого элемента')
# print(list(map(len, c)))
#
# print('Делаем все элементы заглавными')
# print(list(map(str.upper, c)))
#
# print('Выводим каждый элемент списка задом-наперёд при помощи «lambda»')
# print(list(map(lambda x: x[::-1], c)))
# print(list(map(lambda x: x+'!', c)))
#
# print('Это то же самое, но при помощи генератора списков')
# print([i[::-1] for i in c])
#
# b = list(map(list, c))
# print(list(map(list, b)))
# w = list(map(sorted, b))
# print(w)
#
# s = list(map(int, input().split()))
# print(s)
# num = map(int, s)
#
# for i in range(len(s)):
#     print(next(num))
#
# print(sum(s))
#
#
# l = [1, 2, 3, 4]
# print([i for i in l if i % 2 == 0])

with open('numb.txt') as f:
    n = int(f.readline())
    for i in range(n):
        a, b = list(map(int, f.readline().split()))
        print(a, b)

