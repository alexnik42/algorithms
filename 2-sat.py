import sys, threading

sys.setrecursionlimit(800000) # Increase recursion limit for large G (>800k vertices)
threading.stack_size(67108864) # Increase stack size to avoid segmentation fault

G = {}
stack = []

# Process data. Each pair of variables results in 2 edges. 
# For example, for x, y - the first edge will be (-x, y) and the second edge will be (-y, x)
with open('filename.txt', 'r') as file:
    for line in file:
        l = [int(s) for s in line.split()]

        if l[0] > 0 and l[1] > 0:
            if l[0] not in G:
                G[l[0]] = set()

            if -l[0] not in G:
                G[-l[0]] = set({l[1]}) 
            else:
                G[-l[0]].add(l[1])

            if l[1] not in G:
                G[l[1]] = set()

            if -l[1] not in G:
                G[-l[1]] = set({l[0]})
            else:
                G[-l[1]].add(l[0])

        elif l[0] > 0 and l[1] < 0:
            if l[0] not in G:
                G[l[0]] = set() 

            if -l[0] not in G:
                G[-l[0]] = set({l[1]})
            else:
                G[-l[0]].add(l[1])

            if -l[1] not in G:
                G[-l[1]] = set({l[0]})
            else:
                G[-l[1]].add(l[0])

            if l[1] not in G:
                G[l[1]] = set()

        elif l[0] < 0 and l[1] > 0:
            if l[0] not in G:
                G[l[0]] = set()

            if -l[0] not in G:
                G[-l[0]] = set({l[1]})
            else:
                G[-l[0]].add(l[1])

            if -l[1] not in G:
                G[-l[1]] = set({l[0]}) 
            else:
                G[-l[1]].add(l[0])

            if l[1] not in G:
                G[l[1]] = set()

        else:
            if l[0] not in G:
                G[l[0]] = set()

            if -l[0] not in G:
                G[-l[0]] = set({l[1]})
            else:
                G[-l[0]].add(l[1])

            if -l[1] not in G:
                G[-l[1]] = set({l[0]})
            else:
                G[-l[1]].add(l[0])

            if l[1] not in G:
                G[l[1]] = set() 

# Depth-first search, 2 passes
def dfs(G, v, step, V = {}, current_scc = {}):
    global stack

    if (step == 'first_step'): # First pass of Kosaraju's algorithm
        if v not in V:
            V[v] = True
            for e in G[v]:
                dfs(G, e, 'first_step', V)
            stack.append(v)

    else: # Second pass of Kosaraju's algorithm to compute SCC
        
        V[v] = True
        current_scc[v] = True
        for e in G[v]:
            if e not in V:
                dfs(G, e, 'second_step', V, current_scc)


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

# 2-SAT algorithm
def two_sat(G):
    global stack

    # Step 1: Run DFS on G and fill the stack, reverse G
    for v in G:
        dfs(G, v, 'first_step')

    G = reverseGraph(G)

    # Step 2: Run DFS 2nd time, compute SCC and check whether v and -v in the same SCC
    V = {}
    processed_v = {}
    current_scc = {}

    for v in reversed(stack):
        if v not in processed_v:
            current_scc = {}
            dfs(G, v, 'second_step', V, current_scc)

            if -v in current_scc:
                return 'The given instance is unsatisfiable.'

            for key in current_scc:
                if -key in current_scc:
                    return 'The given instance is unsatisfiable.'
                else:
                    processed_v[key] = True

            processed_v[v] = True
            processed_v[-v] = True

    return 'The given instance is satisfiable.'
    

def main():
    print(two_sat(G))

thread = threading.Thread(target=main)
thread.start()