def f(x):
    if x % 2 == 0:
        return x


# l = filter(f, (2, 23, 44, 195, 200))
# print(list(l))


# b = list(map(int, input().split()))
# l = filter(f, b)
# print(list(l))


a = filter(lambda x: (x % 2 == 0), [2, 22, 3])
print(list(a))

