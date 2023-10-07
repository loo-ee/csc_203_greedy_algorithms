from colorama import Fore
from util.util import custom_print, colored_array_print
from number_systems.Calculator import Calculator
from knapsack import knapsack
from huffman_encoding import huffman_encoding


def main():
    choice: int

    while True:
        getting_input = True
        print_menu()

        while getting_input:
            try:
                choice = int(input('Enter choice: '))
            except:
                print("Enter a valid input...")
                continue

            if choice in range(5):
                getting_input = False

        if choice == 0:
            break


        match choice:
            case 1:
                number_systems_calc = Calculator()
                number_systems_calc.run()

            case 2:
                knapsack.run()

            case 3:
                print('Create Egyptian Fractions')

            case 4:
                huffman_encoding.run()
                


def print_menu():
    print('\n*********************************************************************')
    colored_array_print("GREEDY ALGORITHMS", Fore.GREEN, False) 

    print('''

    [0] Exit
    [1] Number Systems Calculator
    [2] Knapsack Algorithm
    [3] Egyptian Fractions
    [4] Huffman Encoding
    ''')


if __name__ == '__main__':
    main()
