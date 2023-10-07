import heapq
import os
from collections import defaultdict

def calculate_frequency(message):
    frequency = defaultdict(int)
    for symbol in message:
        frequency[symbol] += 1
    return frequency

def build_heap(frequency):
    heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    return heap

def merge_nodes(heap):
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return heap

def huffman_encoding(message):
    frequency = calculate_frequency(message)
    heap = build_heap(frequency)
    heap = merge_nodes(heap)
    huff = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
    print("Symbol".ljust(10) + "Weight".ljust(10) + "Huffman Code")
    for p in huff:
        print(p[0].ljust(10) + str(frequency[p[0]]).ljust(10) + p[1])

data = "The frog at the bottom of the well drifts off into the great ocean"
huffman_encoding(data)
