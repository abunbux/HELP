import argparse
import os
import sys

version = "1.0.0"
prog = 'viewing'


# Функция выводит список файлов по заданному пути и
# с указанным расширением.
def build_dict_rename(path, ext):
    list_dir = os.listdir(path)
    exten = ext
    work_dict = {}
    for files in list_dir:
        name, extension = os.path.splitext(files)
        if extension == exten:
            oldname = files
            newname = name + extension
            work_dict[os.path.join(path, oldname)] = os.path.join(path, newname)
    for i in work_dict:
        print(i)
    # return work_dict


# Основная функция.
#     Первым шагом создаём объект ArgumentParser;
#     Затем добавляем аргументы командной строки;
#     Метод parse_args() фактически возвращает некоторые данные из указанных параметров
#         и мы сохраняем их в переменную args и затем обращаемся
#         к ним следующим образом:
#         args.path и args.ext
#    Затем идёт проверка на наличие аргументов при запуске программы
#    и в конце запуск основной функции.
def main():
    parser = argparse.ArgumentParser(description='Description of your program.')
    parser.add_argument('-p', '--path', help='Description for foo argument')
    parser.add_argument('-e', '--ext', help='Description for bar argument')
    args = parser.parse_args()
    if args.path is None:
        parser.error('''Необходимо указать путь к директории.
        Используйте "{0} -h(--help)" для получения справки.'''.format(prog))
    elif args.ext is None:
        parser.error('''Необходимо указать расширение искомых файлов.
        Используйте "{0} -h(--help)" для получения справки.'''.format(prog))
    else:
        build_dict_rename(args.path, args.ext)


# Запуск основной функции с проверкой на ошибки.
if __name__ == '__main__':
    try:
        main()
    except FileNotFoundError:
        print('Вы указали несуществующий путь.')
        sys.exit(0)
    except KeyboardInterrupt:
        print('Программа завершена пользователем.')
        sys.exit(0)
