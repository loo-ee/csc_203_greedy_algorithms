def binary_to_decimal(binary:str):
    decimal_value = 0
    remainder = 0
    factor = 0

    binary_whole = None
    binary_float = ""

    if "." in binary:
        binary_whole, binary_float = binary.split(".")
        binary_whole = int(binary_whole)
    else:
        binary_whole = int(binary)

    while(binary_whole != 0):
        remainder = int(binary_whole % 10)
        binary_whole = int(binary_whole / 10)
        decimal_value += int(remainder * pow(2, factor))
        factor += 1

    factor = 1
    for floating in binary_float:
        current_floating = int(floating)
        decimal_value += current_floating * pow(2, -factor)
        factor += 1

    return str(decimal_value)


def octal_to_decimal(octal:str):
    decimal_value = 0
    remainder = 0
    factor = 0

    octal_whole = None
    octal_float = ""

    if "." in octal:
        octal_whole, octal_float = octal.split(".")
        octal_whole = int(octal_whole)
    else:
        octal_whole = int(octal)

    while(octal_whole != 0):
        remainder = int(octal_whole % 10)
        octal_whole = int(octal_whole / 10)
        decimal_value = int(decimal_value + (remainder * pow(8, factor)))
        factor += 1

    factor = 1
    for floating in octal_float:
        current_floating = int(floating)
        decimal_value += current_floating * pow(8, -factor)
        factor += 1

    return str(decimal_value)


def hexadecimal_to_decimal(hexadecimal:str):
    decimal_value = 0
    hexadecimal_whole = ""
    hexadecimal_float = ""
    hexadecimal_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

    if "." in hexadecimal:
        hexadecimal_whole, hexadecimal_float = hexadecimal.split(".")
    else:
        hexadecimal_whole = hexadecimal

    factor = 0
    for whole in hexadecimal_whole[::-1]:
        whole_index = hexadecimal_list.index(whole)
        decimal_value += int(whole_index * pow(16, factor))
        factor += 1

    factor = 1
    for floating in hexadecimal_float:
        float_index = hexadecimal_list.index(floating)
        decimal_value += float_index * pow(16, -factor)
        factor += 1

    return str(decimal_value)
