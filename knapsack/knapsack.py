from colorama import Fore
from prettytable import PrettyTable
from util.util import colored_array_print


class __Item:
    def __init__(self, name: str, profit: int,  weight: int) -> None:
       self.name = name 
       self.weight = weight
       self.profit = profit

    def __repr__(self) -> str:
        return self.name


def __knapsack_algorithm(items: [__Item], max_weight: int):
    items_values = dict() 
    items_count = dict()
    total_profit = 0

    for item in items:
        value = item.profit / item.weight
        items_values[item] = value

    items_values = dict(sorted(items_values.items(), key=lambda item: item[1], reverse=True))
    items_weight_sum = 0

    for key, value in items_values.items():
        if max_weight == items_weight_sum and max_weight < items_weight_sum: 
            break

        item_adjusted_weight = min(key.weight, max_weight - items_weight_sum)
        item_adjusted_count = item_adjusted_weight / key.weight
        items_count[key] = item_adjusted_count

        items_weight_sum += item_adjusted_weight
        current_item_profit = item_adjusted_count * key.profit
        total_profit += current_item_profit

    print()
    colored_array_print("Items weight sum: ", Fore.YELLOW, False)
    print(f'{items_weight_sum:.3f}')
    colored_array_print("Total profit: ", Fore.GREEN, False)
    print(f'{total_profit:.3f}')
    print()

    return [items_count, items_values]


def run():
    # item1 = __Item('Ballpens', 10, 2)
    # item2 = __Item('Pencils', 5, 3)
    # item3 = __Item('Notebooks', 15, 5)
    # item4 = __Item('Stickers', 7, 7)
    # item5 = __Item('Index Cards', 6, 1)
    # item6 = __Item('Correction Tape', 18, 4)
    # item7 = __Item('Erasers', 3, 1)
 
    # items_array = [item1, item2, item3, item4, item5, item6, item7]
    items_array = [
        __Item('1', 10, 10),
        __Item('2', 20, 5),
        __Item('3', 15, 3),
        __Item('4', 35, 1),
        __Item('5', 5, 2),
        __Item('6', 10, 4),
        __Item('7', 25, 6),
        __Item('8', 15, 5),

    ]
    items_count, items_values = __knapsack_algorithm(items_array, 18)

    computation_table = PrettyTable()
    computation_table.field_names = ['Name', 'Profit', 'Weight', 'P/W', 'Adjusted Weight']

    for element in items_array:
        computation_table.add_row([element.name, element.profit, element.weight, items_values[element], items_count[element]])
        
    print(computation_table)

    print()
    colored_array_print("Included in knapsack: ", Fore.YELLOW, False)
    print()

    included_items_table = PrettyTable()
    included_items_table.field_names = ['Item Name', 'Count']

    for element in items_array:
        found_element_count = items_count[element]

        if found_element_count > 0:
            included_items_table.add_row([element.name, str(round(element.weight * found_element_count))])

    print(included_items_table)
