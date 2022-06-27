# Пример кода из официальной документации разработчика с моими микро-правками:
#
# https://python-watchdog.readthedocs.io/en/stable/quickstart.html#a-simple-example
#
# Следующий пример программы будет рекурсивно отслеживать изменения файловой
# системы в указанном каталоге и просто выводить их на консоль.


# DONE @done Переписать код с использованием argparse.
# CLOSED: [2022-06-28 Tue 00:52]


import logging
import argparse
# import os
from pathlib import Path 
import sys
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    # Здесь идут настройки логирования модуля logging:
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')


    # Настройки argparse:
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path',
                        help='Укажите путь к отслеживаемой директории.',
                        type=str,
                        default='.')
    args = parser.parse_args()

    # Затем определение аргумента командной строки,
    # который должен принять путь к исследуемой директории.
    # Если аргумент не указан - отслеживаем текущую директорию,
    # текущая директория прописана в parser.add_argument:
    path = args.path
    
    # Делаем проверку на существование переданного пути.
    # Здесь два варианта проверки.
    # С помощью модуля os и модуля pathlib.
    # if os.path.exists(path):
    #     if os.path.isfile(path):
    #         logging.info(f'Вы указали путь к файлу {os.path.abspath(path)}')
    #     elif os.path.isdir(path):
    #         logging.info(f'Наблюдаем за каталогом {os.path.abspath(path)}/')
    # else:
    #     logging.info('Объект наблюдения не найден.')
    #     sys.exit()
    
    path_check = Path(path)
    if path_check.exists() and path_check.is_dir():
        logging.info(f'Объект {path_check.cwd()} существует и является директорией.')
    elif path_check.exists() and path_check.is_file():
        logging.info(f'Объект {path_check.cwd()} существует и является файлом.')
    else:
        logging.info(f'Объект {path_check} не наден.')
        sys.exit()

    # Создаём экземпляр класса обработчика,
    # LoggingEventHandler - регистрирует все события:
    event_handler = LoggingEventHandler()
    
    # Создаём экземпляр класса обозревателя:
    observer = Observer()

    # Вызываем функцию расписания через экземпляр наблюдателя
    # observer.schedule(), передавая в неё экземпляр класса
    # LoggingEventHandler(), он сопоставлен с переменной
    # event_handler, путь - path, который получаем через аргумент
    # командной строки и указываем, что наблюдать нужно рекурсивно:
    observer.schedule(event_handler, path, recursive=True)

    # Запускаем обозревател
    observer.start()

    try:
        while observer.is_alive():
            observer.join(1)
    except KeyboardInterrupt:
        logging.info('Операция завершена пользователем.')
    finally:
        observer.stop()
        observer.join()
