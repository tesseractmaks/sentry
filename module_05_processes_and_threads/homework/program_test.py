import sys


def main():
    user_input = input()
    print('Print to stdout')
    print('Print to stderr', file=sys.stderr)

    print(user_input)


if __name__ == '__main__':
    main()