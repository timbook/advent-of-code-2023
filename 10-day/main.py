import numpy as np
import networkx as nx

# data_raw = np.loadtxt('data/sample.txt', dtype=str, comments=None)
data_raw = np.loadtxt('data/input.txt', dtype=str, comments=None)
data = np.array([list(row) for row in data_raw])
R, C = data.shape

x, y = np.where(data == 'S')
S = (x[0], y[0])

data[S[0], S[1]] = 'F'
visited = []
to_explore = [S]

while to_explore:
    curr_node = to_explore.pop()
    val = data[curr_node[0], curr_node[1]]
    
    # Go right?
    if val in '-LF':
        next_node = (curr_node[0], curr_node[1] + 1)
        if next_node not in visited:
            to_explore.append(next_node)
            
    # Go left?
    if val in '-J7':
        next_node = (curr_node[0], curr_node[1] - 1)
        if next_node not in visited:
            to_explore.append(next_node)
    
    # Go up?
    if val in '|LJ':
        next_node = (curr_node[0] - 1, curr_node[1])
        if next_node not in visited:
            to_explore.append(next_node)
            
    # Go down?
    if val in '|7F':
        next_node = (curr_node[0] + 1, curr_node[1])
        if next_node not in visited:
            to_explore.append(next_node)
    
    visited.append(curr_node)

visited = list(set(visited))
sol = len(visited) // 2

print(f"A ::: {sol}")
