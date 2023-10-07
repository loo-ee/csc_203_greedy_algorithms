from binarytree import build, Node
from colorama import Fore
from prettytable import PrettyTable


class __TreeNode:
    def __init__(self, data: str, freq: int) -> None:
        self.data = data
        self.freq = freq
        self.left = self.right = None


def __generate_tree(data: []):
    while len(data) != 1:
        left_node = data[0]
        del data[0]
        right_node = data[0]
        del data[0]

        node = __TreeNode('$', left_node.freq + right_node.freq)
        node.left = left_node
        node.right = right_node

        data.append(node)
        data.sort(key=lambda node: node.freq)

    return data[0]


def print_codes(root: __TreeNode, tree_list: [], top: int, tree_root: Node, codes_dict: dict):
    if root.left is not None:
        tree_list[top] = '0'

        tree_root.left = Node(root.left.data + '-' + str(root.left.freq))
        print_codes(root.left, tree_list, top + 1, tree_root.left, codes_dict)

    if root.right is not None:
        tree_list[top] = '1'
        tree_root.right = Node(root.right.data + '-' + str(root.right.freq))
        print_codes(root.right, tree_list, top + 1, tree_root.right, codes_dict)

    if root.left is None and root.right is None:
        value_str = ""
        
        for i in range(top):
            value_str += str(tree_list[i])

        codes_dict[root.data] = str(value_str)

    
def __HuffmanCodes(data: [], freqs: []):
    sorted_data = []
    codes_dict = dict()
    
    for i in range(len(data)):
        new_Tree_Node = __TreeNode(data[i], freqs[i])
        sorted_data.append(new_Tree_Node) 

    sorted_data.sort(key=lambda node: node.freq)

    root = __generate_tree(sorted_data[:])
    tree_list = [None] * 100 

    print('\nLeft is ', end="")
    print(Fore.GREEN, '1', end="")
    print(Fore.WHITE)
    print("Right is", end="")
    print(Fore.WHITE, end="")
    print(Fore.RED, '0')
    print(Fore.WHITE)

    tree_root = Node(root.data + '-' + str(root.freq))
    print_codes(root, tree_list, 0, tree_root, codes_dict)
    print(tree_root)

    table = PrettyTable()
    table.field_names = ['8 bit ASCII', 'Huffman Encoded']

    for key, value in codes_dict.items():
        table.add_row([key, value])

    print(table)


def extract_freq(data: str):
    data_freq_dict = dict()
    freqs = []
    cleaned_data = []

    for element in data:
        if element == ' ':
            continue

        if element in data_freq_dict:
            data_freq_dict[element] += 1
        else:
            data_freq_dict[element] = 1

    for key, value in data_freq_dict.items():
        cleaned_data.append(key)
        freqs.append(value)
    
    return [cleaned_data, freqs]


def run():
    # data = "Negros Oriental State University Main Campus Dumaguete City"
    data = input("Enter word or phrase here: ")
    cleaned_data, freqs = extract_freq(data.lower())
    __HuffmanCodes(cleaned_data, freqs)
