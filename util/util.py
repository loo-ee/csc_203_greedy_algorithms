from colorama import Fore, Back, Style, init


def find_target():
    try:
        target = int(input("Enter target: "))
        return target
    except:
        print("[ERROR] Target must be an integer")


def swap(array: list, x_pos: int, y_pos: int):
    temp = array[x_pos]
    array[x_pos] = array[y_pos]
    array[y_pos] = temp


def get_input():
    input_arr = []

    while True:
    
        try:
            num = int(input('Enter number: '))
            input_arr.append(num)
        except:
            break

    return input_arr


def custom_print(array: list, green_values: [int], red_values: [int], blue_values: [int] = None):
    init()
    print('[', end="")

    for i in range(len(array)):
        if array[i] in green_values:
            print(Fore.GREEN, array[i], end="")
        elif array[i] in red_values:
            print(Fore.RED, array[i], end="")
        elif blue_values is not None and array[i] in blue_values:
            print(Fore.BLUE, array[i], end="")
        else:
            print(Fore.WHITE, array[i], end="")

        if i != len(array) - 1:
            print(Fore.WHITE, ', ', end="")

    print(Style.RESET_ALL, end="")
    print(']', end="\t\t\t")


def colored_array_print(array: list, colorama_clr: str, separated: bool = True):
    init()
    
    if separated:
        print('[', end="")

    for i in range(len(array)):
        print(colorama_clr, array[i], end="")

        if i != len(array) - 1 and separated:
            print(', ', end="")

    print(Style.RESET_ALL, end="")

    if separated:
        print(']', end='') 
