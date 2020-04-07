import sys, threading

sys.setrecursionlimit(800000) # Increase recursion limit for large G (>800k vertices)
threading.stack_size(67108864) # Increase stack size to avoid segmentation fault

G = {} # Set initial G
G_rvr = {} # Set reversed G
V = {} # Set object for tracking visited nodes in G
V_rvr = {} # Set object for tracking visited nodes in G_rvr
t = 0 # Track finishing times in 1st pass of depth-first search
counter_scc = 0 # Counter of SCC's
scc_list = [] # List of all SCC's

# Open file and transform it to Dict
with open('filename.txt', 'r') as file:
    for line in file:
        l = [int(s) for s in line.split()] # Read each line as List of integers

        if l[0] not in G: # Create new node if node is not in G
            G[l[0]] = {'edges': l[1:], 't': 0} 
            V[l[0]] = False 

            if l[1] not in G: # Create new node if other node is not in G (in case node does not have any forward directions)
                G[l[1]] = {'edges': [], 't': 0} 
                V[l[1]] = False

        else:
            if l[1] not in G:
                G[l[1]] = {'edges': [], 't': 0} 
                V[l[1]] = False
            G[l[0]]['edges'].append(l[1])

# Depth-first search 
def depth_first_search(G, n, V, step):
    global t
    global counter_scc

    if (step == 'first'): # First pass of kosaraju's algorithm
        V[n] = True # Mark n as visited

        if (len(G[n]['edges']) > 0): # Check if node has forward directions
            for i in range(len(G[n]['edges'])):
                if V[G[n]['edges'][i]] == False:
                    depth_first_search(G, G[n]['edges'][i], V, 'first') # Proceed in the forward direction if node is not explored

        t += 1 # Increment finishing time
        G[n]['t'] = t # Assign new order's number to the node

    else: # Second pass of kosaraju's algorithm to compute SCC's
        V[n] = True

        if (len(G[n]['edges']) > 0):
            for i in range(len(G[n]['edges'])):
                if V[G[n]['edges'][i]] == False:
                    counter_scc += 1
                    depth_first_search(G, G[n]['edges'][i], V, 'second')

# Kosaraju algorithm
def kosaraju(G):
    global counter_scc

    n = list(G.keys())[-1] # Define number of vertices in G

    # Step 1: Run DFS on G and mark new order of nodes
    for i in range(n, 0, -1): # Iterate through nodes in G
        if i in G: # Avoid missing nodes
            if V[i] == False:
                depth_first_search(G, i, V, 'first')

    # Step 2: define G_rvr with new order of nodes and reversed directions
    for item, value in G.items():
        for i in range(len(value['edges'])): # Iterate through edges of node
            if not G[value['edges'][i]]['t'] in G_rvr:
                # Switch existing nodes with their respective t's and reverse the direction  
                G_rvr[G[value['edges'][i]]['t']] = {'edges':[]}
                G_rvr[G[value['edges'][i]]['t']]['edges'].append(value['t'])
            else:
                G_rvr[G[value['edges'][i]]['t']]['edges'].append(value['t'])

    # Step 2.1: include in G_rvr nodes with no forward directions
    for i in range(1, n + 1):
        if i not in G_rvr and i in G:
            G_rvr[i] = {'edges': []} 

    # Step 2.2: mark all nodes in G_rvr as unvisited
    for item, value in G_rvr.items():
        V_rvr[item] = False

    # Step 3: run depth-first search for each node in G_rvr to calculate SCC's
    for i in range(n, 0, -1):
        if i in G_rvr:
            counter_scc = 0
            if V_rvr[i] == False:
                counter_scc += 1
                depth_first_search(G_rvr, i, V_rvr, 'second')

            if counter_scc != 0: # Avoid zero counter
                scc_list.append(counter_scc) # Append found SCC's to the List of SCC's

# Main function
def main():
    kosaraju(G) # Run kosaraju's algorithm

    top5_scc = sorted(scc_list, reverse=True)
    print(top5_scc[:5]) # Output top-5 SCC's

# Run code
thread = threading.Thread(target=main)
thread.start()