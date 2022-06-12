# CREATED: <Sun Jun 12 15:49:38 EEST 2022>
# Time-stamp: <Последнее обновление -- Sunday June 12 20:36:52 EEST 2022>

# @todo Написать скрипт создания директории и записи файла в эту директорию
#  с логированием действий (logging) и получением аргументов командной строки (argparse),
#  которые передают место ,имя файла и строку, которую нужно записать в этот файл.

# В грубой форме скрипт, конечно же, готов, но кое-чего не хватает:
# @todo Оформить функции;
# @todo Осуществить отлов исключений.

import logging
import argparse
from pathlib import Path

# Настройка логирования:
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# Настройка парсера аргументов командной строки:
parser = argparse.ArgumentParser(description='''Программа делает запись в указанный
файл в указанной папке. Аргументы передаются в командной строке.''')
parser.add_argument('-p', '--path', type=str, default='.',
                    help='''Укажите путь к директории.
Если её не существует - она будет создана.''')
parser.add_argument('-f', '--file', type=str, default='file.txt',
                    help='''Укажите имя создаваемого файла.''')
parser.add_argument('-t', '--text', type=str, help='''Какой текст Вы бы желали записать в файл?''',
                    default='Как же долго я этого ждал.\n')

args = parser.parse_args()

# Принимаем путь к директории в виде аргумента:
path = Path(args.path)
# Выводим сообщение о передаваемом пути:
if args.path == '.':
    logging.info('Переданный путь является текущей директорией.')
else:
    logging.info(f'Переданный путь {path}')

# Принимаем имя файла:
path_file = Path(path, args.file)
# И выводим сообщение с этим именем:
logging.info(f'Имя файла {args.file}')

# Проверяем указанный путь на существование, а если он существует,
# делаем заявление и запись:
if path.exists() and path.is_dir():
    logging.info('Директория уже существует, делаем запись.')
    path_file.open('a').write(args.text)
else:
    # Если каталог отсутствует, объявляем, создаём его
    # и делаем запись в файл:
    logging.info('Директория не существует.')
    path.mkdir(parents=True, exist_ok=True)
    logging.info('Создаём её и делаем запись.')
    path_file.open('a').write(args.text)
