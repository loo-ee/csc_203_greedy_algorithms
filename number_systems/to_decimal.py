def binary_to_decimal(binary:int):
    decimal_value = 0
    remainder = 0
    factor = 0

    while(binary != 0):
        remainder = int(binary % 10)
        binary = int(binary / 10)
        decimal_value += int(remainder * pow(2, factor))
        factor += 1

    return decimal_value


def octal_to_decimal(octal:int):
    decimal_value = 0
    remainder = 0
    factor = 0

    while(octal != 0):
        remainder = int(octal % 10)
        octal = int(octal / 10)
        decimal_value = int(decimal_value + (remainder * pow(8, factor)))
        factor += 1

    return decimal_value


def hexadecimal_to_decimal(hexadecimal:str):
    decimal = int(hexadecimal, 16)
    return decimal
