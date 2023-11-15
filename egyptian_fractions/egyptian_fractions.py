from colorama import Fore
from util.util import colored_array_print


def __printEgyptian(nr, dr):
    if nr == 0 or dr == 0:
        return

    if dr % nr == 0:
        print(f'1/{dr//nr}')
        return

    if nr % dr == 0:
        print(f'{nr//dr}')
        return

    if nr > dr:
        print(f'{nr//dr} + ', end="")
        __printEgyptian(nr%dr, dr)
        return

    n = dr//nr + 1
    print(f'1/{n} + ', end="")
    __printEgyptian(nr*n-dr, dr*n)

def run():
    numerator = int(input("\nEnter numerator: "))
    denominator = int(input("Enter denominator: "))

    print()
    colored_array_print("Egyptian Fraction Representation of " + str(numerator) + " / " + str(denominator) + " is ", Fore.YELLOW, False)
    print()
    __printEgyptian(numerator, denominator)
