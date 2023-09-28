def find_shortest_path(graph, initial_state, goal):
    states = [[initial_state]]
    while states:
        path = states.pop(0)
        node = path[-1]
        for adjacent in graph[node]:
            if check_validity(path, adjacent) and check_duplicate_edges(path, adjacent):
                new_path = list(path)
                if adjacent == goal:
                    return len(path)
                new_path.append(adjacent)
                states.append(new_path)
    return -1


def check_duplicate_edges(path, adjacent):
    for i in range(len(path) - 1):
        if path[i] == path[-1] and path[i + 1] == adjacent:
            return False
    return True


def check_validity(path, adjacent):
    if len(path) >= 2:
        t = (path[-2], path[-1], adjacent)
        if t in tuples:
            return False
    return True


n, m, k = map(int, input().split())
g = [[] for i in range(n)]
depth_limit = 2 * n
for i in range(m):
    x, y = map(int, input().split())
    g[x - 1].append(y - 1)
    g[y - 1].append(x - 1)
tuples = set()
for i in range(k):
    tuples.add(tuple(int(x) - 1 for x in input().split()))
print(find_shortest_path(g, 0, n - 1))
