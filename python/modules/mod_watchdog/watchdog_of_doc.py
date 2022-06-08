# Пример кода из официальной документации разработчика с моими микро-правками:
#
# https://python-watchdog.readthedocs.io/en/stable/quickstart.html#a-simple-example
#
# Следующий пример программы будет рекурсивно отслеживать изменения файловой системы в указанном каталоге
# и просто выводить их на консоль.


# TODO Переписать код с использованием argparse и изменить настройки logging.
#    DEADLINE: <2022-06-12 Sun>


import logging
import argparse
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    # Настройки argparse:
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path',
                        help='Укажите путь к отслеживаемой директории.',
                        type=str)
    args = parser.parse_args()

    # Затем определение аргумента командной строки,
    # который должен принять путь к исследуемой директории.
    # Если аргумент не указан - отслеживаем текущую директорию:
    path = args.path if args.path != 0 else '.'

    # Сперва идут настройки логирования модуля logging:
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Создаём экземпляр класса обработчика,
    # LoggingEventHandler - регистрирует все события:
    event_handler = LoggingEventHandler()

    # Создаём экземпляр класса обозревателя:
    observer = Observer()

    # Вызываем функцию расписания через экземпляр наблюдателя observer.schedule(),
    # передавая в неё экземпляр класса LoggingEventHandler(), он сопоставлен с переменной
    # event_handler, путь - path, который получаем через аргумент командной строки
    # и указываем, что наблюдать нужно рекурсивно:
    observer.schedule(event_handler, path, recursive=True)

    # Запускаем обозреватель:
    observer.start()
    try:
        while observer.is_alive():
            observer.join(1)
    except KeyboardInterrupt:
        logging.info('Операция завершена пользователем.')
    finally:
        observer.stop()
        observer.join()
