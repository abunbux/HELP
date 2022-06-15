from pathlib import Path
import argparse
import sys


# На первый взгляд, пожалуй, этот скрипт имеет тот же функционал, что и mod_os-viewing.py,
# только с использованием модуля pathlib, но благодаря rglob выполняет задачу рекурсивно
# да и кода заметно меньше.

# Просмотр директорий и файлов по заданным параметрам.
# Скрипт принимает аргумент с указанием пути к директории (по-умолчанию, откуда запускается скрипт)
# и аргумент с расширением файлов, список которых нужно вывести на экран.

def viewing(path, ext):
    for files in Path(path).rglob(ext):
        print(files)


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('-p', '--path', default='.', help="Укажите путь к директории.")
    parse.add_argument('-e', '--ext', required=True, help="Укажите расширение выводимых файлов.")
    args = parse.parse_args()
    viewing(args.path, '*' + args.ext)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Программа завершена пользователем.')
        sys.exit(0)
