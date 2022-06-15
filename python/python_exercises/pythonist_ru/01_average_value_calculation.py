# Программа принимает введенные по одному числа, которые сохраняются в список.
# Затем она выводит среднее значение всех элементов этого списка.


while True:
    try:
        count = int(input('Сколько чисел будем использовать? '))
    except ValueError:
        print('Это не совсем число. Попробуйте снова.')
    else:
        print(f'Вы ввели {count}')
        break


print('Сейчас я буду запрашивать у Вас числовые значения.')
a = []


for i in range(0, count):
    while True:
        try:
            n = int(input('Введите число '))
            a.append(n)
        except ValueError:
            print('Это не совсем число. Попробуйте снова.')
        else:
            break


average = sum(a) / count
print('Среднее значение', round(average, 2))
