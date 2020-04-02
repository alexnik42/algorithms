import random, math, copy

G = {}

# Open file and transform it to Dict
with open('test.txt', 'r') as file:
    for line in file:
        l = [int(s) for s in line.split()] # Convert file to List, which contain Lists with numbers
        G[l[0]] = l[1:] # Convert List to Dict, where first item is key and others are List of values

# Karger's algorithm
def karger(G):

    while len(G) > 2:

        v = random.choice(list(G.keys())) # Pick random vertex
        u = random.choice(list(G[v])) # Pick random edge based on chosen vertex

        G[v].extend(G[u]) # Copy edges from u to v

        for value in G[u]: # Iterate through edges of u

            G[value].remove(u)
            G[value].append(v)

        G[v] = [num for num in G[v] if num != v] # Eliminate all self-loops

        del G[u]

    return len(list(G.values())[0]) # Return edges between two remaining vertices

# Iterate the algorithm sufficient number of times to find a min cut
def trials(G):

    counter = 0
    n = len(G)*math.log(len(G), 10) # Works fine for 200 vertices, use n^2 * ln(x) for (1 - 1/n) prob. of success
    min_edges = len(G) - 1 # Set the highest bound for number of edges

    while counter < n:
        trial_G = copy.deepcopy(G)
        min_edges = min(min_edges, karger(trial_G))
        counter += 1

    return min_edges

print(trials(G))