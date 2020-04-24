'''

This algorithm calculates the largest value of k such that there is a k-clustering with spacing at least 3.

The format of data set is:

[first bit of node 1] ... [last bit of node 1]
...
[first bit of node n] ... [last bit of node n]

The distance between two nodes u and v in this problem is defined as the Hamming distance (number of differing bits between the two nodes). 
For example, the Hamming distance between the 24-bit labels of 2 nodes below is 3 (since they differ in the 3rd, 7th, and 21st bits):
"0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1" (node #1)
"0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" (node #2)
_________________________________________________
"0 0 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0" 


This algorithm uses NetWorkX package for UnionFind data structure. 
Source code: https://networkx.github.io/documentation/stable/_modules/networkx/utils/union_find.html. License - https://networkx.github.io/documentation/stable/license.html

'''

from networkx.utils.union_find import UnionFind

G = []
V = {}
n_bits = 24
distances = [0] # An array of bit-masks for the distances

# Calculate bit-masks for distances < 3 
[distances.append(1 << i) for i in range(n_bits)] # Distances equal to 1

for i in range(0, n_bits - 1): # Distances equal to 2
    d_1 = 1 << i
    for j in range(i+1, n_bits):
        d_2 = 1 << j
        distances.append(d_1^d_2)

# Read input file
with open('file_name.txt', 'r') as file:
    for line in file:
        l = [s for s in line.split()]
        G.append(int(''.join(l), 2)) # Convert each node from binary to integer

for i in range(len(G)):
    if G[i] not in V:
        V[G[i]] = set()
        V[G[i]].add(i)
    else:
        V[G[i]].add(i)

# Initialize UnionFind-instance
my_set = set([i for i in range(len(G))])
u_find = UnionFind(my_set)

# Iterate through nodes and distances, XOR each key with the distances to check, whether the resulting node exists. 
# If yes - call union() to merge their respective sets in UnionFind
for key_1, value in V.items():
    for i in range(len(distances)):
        key_2 = key_1^distances[i]

        if key_2 in V:
            for value_1 in V[key_1]:
                for value_2 in V[key_2]:
                    u_find.union(value_1, value_2)

# Create a set of clusters' names and output their quantity (k)
names_of_clusters = set([u_find[x] for x in my_set])
k = len(names_of_clusters) 
print(k)
