import argparse
import sys

parse = argparse.ArgumentParser()
parse.add_argument('l', help='Аргумент «l».', type=int)
parse.add_argument('b', help='Аргумент «b».', type=int)
parse.add_argument('--action', help='Аргумент «--action».', default="sumarize")
args = parse.parse_args()
print(args)
print('Аргумент l = ' + str(args.a))
print('Аргумент b = ' + str(args.b))


def sumarize(a, b):
    print(a + b)


def minusize(a, b):
    print(a - b)


if __name__ == '__main__':
    try:
        if args.action == 'sumarize':
            sumarize(args.a, args.b)
        elif args.action == 'minusize':
            minusize(args.a, args.b)
    except TypeError:
        print('Упс! Что-то пошло не так...')
        print('Небось аргументы забыл, да?')
        sys.exit(0)
    except KeyboardInterrupt:
        print('Программа завершена пользователем.')
        sys.exit(0)
