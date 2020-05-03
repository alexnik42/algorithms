'''
Huffman's algorithm - an algorithm to obtain optimal codes (in binary form) for symbols given their frequences with running time of O(n log n)

Input data format:
    [weight of symbol #1]
    ...
    [weight of symbol n]

Code below can be modified to incorporate different symbols' names by changing 'Read data to heap' section

Algorithm outputs max and min bit's length and list of symbols with corresponding codes
'''

import heapq

heap = []
codes = {}

# Read data to heap
with open('filename.txt', 'r') as file:
    i = 0
    for line in file:
        heapq.heappush(heap, (int(line.strip('\n')), str(i)))
        i += 1

# Construct tree with all symbols
def createTree(heap) :
    while len(heap) > 1: 
        
        li = heapq.heappop(heap) # Eliminate first minimum freq
        hi = heapq.heappop(heap) # Eliminate second minimum freq

        heapq.heappush(heap, (li[0] + hi[0], (li, hi))) # Add sum of two lowest freq to heap

    return heap[0]

# Eliminate frequencies 
def eliminateFreq(tree) :
    p = tree[1]
    if type(p) == str: # Keep symbols, otherwise recurse
        return p
    else: 
        return (eliminateFreq(p[0]), eliminateFreq(p[1]))

# Assign codes to symbols by recursion
def setCodes(node, bits='') :
    global codes
    if type(node) == str: # Assign code if reach a symbol, otherwise recurse and increase code by 0 or 1
        codes[node] = bits                
    else:
        setCodes(node[0], bits+"0")
        setCodes(node[1], bits+"1")

# Huffman's Algorithm
def huffman(heap):
    tree = createTree(heap)
    tree_without_freq = eliminateFreq(tree)
    setCodes(tree_without_freq)

# Run algorithm and sort symbols by bite's length
huffman(heap)
sorted_codes = sorted(codes.items(), key=lambda item: len(item[1]))

# Print the results
print("Maximum bit's length: " + str(len(sorted_codes[-1][1])) + " bit(s)")
print("Minimum bit's length: " + str(len(sorted_codes[0][1])) + " bit(s)")
print('')
print("List of symbols and corresponding codes:")

for symbol in sorted_codes:
    print("Symbol " + symbol[0] + ": " + symbol[1])