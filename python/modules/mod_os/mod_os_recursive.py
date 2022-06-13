import os

path = '/home/abunbux/Видео'


def recursive(directory, level=1):
    print('Уровень =', level, 'Content: ', os.listdir(directory))
    for i in os.listdir(directory):
        if os.path.isdir(directory + '/' + i):
            print('Спускаемся ниже в ', directory + '/' + i)
            recursive(directory + '/' + i, level + 1)
            print('Возвращаемся в ', directory)


recursive(path)
