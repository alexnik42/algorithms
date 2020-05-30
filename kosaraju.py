import sys, threading

sys.setrecursionlimit(800000) # Increase recursion limit for large G (>800k vertices)
threading.stack_size(67108864) # Increase stack size to avoid segmentation fault

G = {}
stack = []

# Process data
with open('filename.txt', 'r') as file:
    for line in file:
        l = [int(s) for s in line.split()]

        if l[0] not in G:
            G[l[0]] = set({l[1]})

            if l[1] not in G: # In case v does not have any forward directions
                G[l[1]] = set()

        else:
            G[l[0]].add(l[1])

            if l[1] not in G:
                G[l[1]] = set()

# Depth-first search, 2 passes
def dfs(G, v, step, V = {}, scc_count = 0):
    global stack

    if (step == 'first_step'): # First pass of Kosaraju's algorithm
        if v not in V:
            V[v] = True
            for e in G[v]:
                dfs(G, e, 'first_step', V)
            stack.append(v)

    else: # Second pass of Kosaraju's algorithm to compute SCCs sizes
        
        V[v] = True
        scc_count += 1
        for e in G[v]:
            if e not in V:
                res = dfs(G, e, 'second_step', V, scc_count)
                scc_count = res[0]
                V = res[1]

        return scc_count, V

# Reverse directions of all edges
def reverseGraph(G):

    G_reversed = {}
    
    for v in G:
        for e in G[v]:
            if e not in G_reversed:
                G_reversed[e] = set({v})
            else:
                G_reversed[e].add(v)

        if v not in G_reversed:
            G_reversed[v] = set({})

    return G_reversed

# Kosaraju's algorithm
def kosaraju(G):
    global stack

    # Step 1: Run DFS on G and fill the stack
    for v in G:
        dfs(G, v, 'first_step')

    G = reverseGraph(G)
    scc_list = []
    V = {}

    # Step 2: Calculate the size of each SCC and append it to the list of all SCCs sizes
    for v in reversed(stack):
        if v not in V:
            res = dfs(G, v, 'second_step', V)
            scc_list.append(res[0])
            V = res[1]

    return scc_list

def main():
    scc_list = kosaraju(G)
    print "Five largest sizes of SCCs in G: {}".format(sorted(scc_list, reverse=True)[:5])

thread = threading.Thread(target=main)
thread.start()
