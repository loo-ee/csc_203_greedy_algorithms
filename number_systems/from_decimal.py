def decimal_to_binary(decimal: str):
    decimal_clone: int
    decimal_clone_float = ""

    if "." in decimal:
        decimal_clone, decimal_clone_float = decimal.split(".")
        decimal_clone = int(decimal_clone)
        decimal_clone_float = float("0." + decimal_clone_float)
    else:
        decimal_clone = int(decimal)

    multiplier = 1
    binary_value = 0
    binary_float_value = ""

    while decimal_clone != 0:
        binary_value = int(binary_value + (decimal_clone % 2) * multiplier)
        decimal_clone = int(decimal_clone / 2)
        multiplier *= 10

    limit = 10
    while decimal_clone_float != 0.0 and decimal_clone_float != "" and limit != 0:
        res = decimal_clone_float * 2
        res_str = str(res)
        whole, floating = res_str.split(".") 
        binary_float_value += whole
        decimal_clone_float = float("0." + floating)
        limit -= 1

    if limit == 10:
        return str(binary_value)

    return str(binary_value) + "." + str(binary_float_value)


def decimal_to_octal(decimal:str):
    decimal_clone: int 
    decimal_clone_float = ""

    if "." in decimal:
        decimal_clone, decimal_clone_float = decimal.split(".")
        decimal_clone = int(decimal_clone)
        decimal_clone_float = float("0." + decimal_clone_float)
    else:
        decimal_clone = int(decimal)

    multiplier = 1
    octal_value = 0
    octal_float_value = ""

    while(decimal_clone != 0):
        octal_value = int(octal_value + (decimal_clone % 8) * multiplier)
        decimal_clone = int(decimal_clone / 8)
        multiplier *= 10

    limit = 10
    while decimal_clone_float != 0.0 and decimal_clone_float != "" and limit != 0:
        res = decimal_clone_float * 8
        res_str = str(res)
        whole, floating = res_str.split(".") 
        octal_float_value += whole
        decimal_clone_float = float("0." + floating)
        limit -= 1

    if limit == 10:
        return str(octal_value)

    return str(octal_value) + "." + str(octal_float_value)


def decimal_to_hexadecimal(decimal:str):
    decimal_clone: int
    decimal_clone_float = ""

    if "." in decimal:
        decimal_clone, decimal_clone_float = decimal.split(".")
        decimal_clone = int(decimal_clone)
        decimal_clone_float = float("0." + decimal_clone_float)
    else:
        decimal_clone = int(decimal)

    hexadecimal_value= ''
    hexadecimal_float_value = ""
    hexadecimal_list = []
    hexadecimal_float_list = []
    hexadecimal_map = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

    while decimal_clone != 0:
        hexadecimal_list.append(int(decimal_clone % 16))
        decimal_clone = int(decimal_clone / 16)

    limit = 10
    while decimal_clone_float != 0.0 and decimal_clone_float != "" and limit != 0:
        res = decimal_clone_float * 16
        res_str = str(res)
        whole, floating = res_str.split(".") 
        hexadecimal_float_list.append(int(whole))
        decimal_clone_float = float("0." + floating)
        limit -= 1

    for i in range(len(hexadecimal_list)):
        hexadecimal_value += hexadecimal_map[hexadecimal_list[i]]

    for i in range(len(hexadecimal_float_list)):
        hexadecimal_float_value += hexadecimal_map[hexadecimal_float_list[i]]

    if limit == 10:
        return hexadecimal_value[::-1]

    return hexadecimal_value[::-1] + "." + hexadecimal_float_value
    