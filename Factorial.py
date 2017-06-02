import sys


def fact(n):
    """
    factorial fun a func written for unittest
    :param n: int num
    :return: n's factorial

    """
    if n == 0:
        return 1

    return n * fact(n - 1)


def div(n):
    """
    division
    """
    return 10 / n


def main(n):
    print(fact(n))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
