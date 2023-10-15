from colorama import Fore
from util.util import custom_print, colored_array_print
from number_systems.Calculator import Calculator
from knapsack import knapsack
from egyptian_fractions import egyptian_fractions
from huffman_encoding import huffman_encoding
from activity_selection import activity_selection
from job_selection import job_selection


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

            if choice in range(7):
                getting_input = False

        match choice:
            case 0:
                break

            case 1:
                number_systems_calc = Calculator()
                number_systems_calc.run()

            case 2:
                knapsack.run()

            case 3:
                egyptian_fractions.run()

            case 4:
                huffman_encoding.run()
            
            case 5:
                activity_selection.run()

            case 6:
                job_selection.run()


def print_menu():
    print('\n*********************************************************************')
    colored_array_print("GREEDY ALGORITHMS", Fore.GREEN, False) 

    print('''

    [0] Exit
    [1] Number Systems Calculator
    [2] Knapsack Algorithm
    [3] Egyptian Fractions
    [4] Huffman Encoding
    [5] Activity Selection
    [6] Job Selection
    ''')


if __name__ == '__main__':
    main()
