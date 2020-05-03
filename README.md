# Algorithms

My implementation of popular algorithms in Python 3:


**Divide-and-conquer algorithms**

* Randomized QuickSort algorithm (1961) - a commonly used algorithm for sorting with average running time of O(*n* log *n*). It works by randomly selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively. [[Description](https://en.wikipedia.org/wiki/Quicksort)] [[Code](./randomized_quick_sort.py)]


**Randomized algorithms**

* Karger's algorithm (1993) - computation of a minimum cut of a connected graph based on the concept of contraction of an edge (v,u) in an undirected graph G=(V,E). [[Description](https://en.wikipedia.org/wiki/Karger%27s_algorithm)] [[Code](./karger.py)]

**Graph search**

* Kosaraju's algorithm (1978) - an algorithm to find the strongly connected components [[Wiki](https://en.wikipedia.org/wiki/Strongly_connected_component)] of a directed graph using two passes of depth-first search with linear running time of O(n + m), which is asymptotically optimal because there is a matching lower bound (any algorithm must examine all vertices and edges). [[Description](https://en.wikipedia.org/wiki/Kosaraju's_algorithm)] [[Code](./kosaraju.py)]

**Greedy algorithms**

* Clustering - an algorithm to calculate the largest value of k such that there is a k-clustering with spacing at least 3 (can be easily modified to use different spacing condition) with nodes represented in binary form. [[Description](https://en.wikipedia.org/wiki/Cluster_analysis)] [[Code](./clustering.py)]
* Huffman's algorithm (1952) - an algorithm to obtain optimal codes (in binary form) for symbols given their frequences with running time of O(*n* log *n*). Implementation using heap and recursion. [[Description](https://en.wikipedia.org/wiki/Huffman_coding)] [[Code](./huffman.py)]
