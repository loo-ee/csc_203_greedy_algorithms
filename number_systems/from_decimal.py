def decimal_to_binary(decimal:int):
    decimal_clone = decimal
    multiplier = 1
    binary_value = 0

    while decimal_clone != 0:
        binary_value = int(binary_value + (decimal_clone % 2) * multiplier)
        decimal_clone = int(decimal_clone / 2)
        multiplier *= 10

    return binary_value


def decimal_to_octal(decimal:int):
    decimal_clone = decimal
    multiplier = 1
    octal_value = 0

    while(decimal_clone != 0):
        octal_value = int(octal_value + (decimal_clone % 8) * multiplier)
        decimal_clone = int(decimal_clone / 8)
        multiplier *= 10

    return octal_value


def decimal_to_hexadecimal(decimal:int):
    decimal_clone = decimal
    hexadecimal_value= ''
    hexadecimal_list = []
    hexadecimal_map = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

    while decimal_clone != 0:
        hexadecimal_list.append(int(decimal_clone % 16))
        decimal_clone = int(decimal_clone / 16)

    for i in range(len(hexadecimal_list)):
        hexadecimal_value += hexadecimal_map[hexadecimal_list[i]]

    return hexadecimal_value [::-1]
    