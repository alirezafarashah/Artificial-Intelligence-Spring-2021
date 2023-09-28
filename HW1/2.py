from queue import PriorityQueue


class Node:
    def __init__(self, h, g, location):
        self.location = location
        self.parent = None
        self.h = h
        self.g = g

    def __lt__(self, other):
        return self.h + self.g < other.h + other.g

    def __eq__(self, other):
        return self.location == other.location

    def set_parent(self, parent):
        self.parent = parent


def a_star_search(my_map, pac_X, pac_Y):
    fringe = PriorityQueue()
    closed = set()
    fringe.put(Node(manhattan_distance(pac_X, pac_Y), 0, (pac_X, pac_Y)))
    while not fringe.empty():
        current = fringe.get()
        coordinates = current.location
        if current.location in closed:
            continue
        if coordinates == (goalX, goalY):
            path = []
            while current:
                path.append(current.location)
                current = current.parent
            return path[::-1]
        closed.add(current.location)

        if coordinates[0] - 1 >= 0 and my_map[coordinates[0] - 1][coordinates[1]] != '%':
            manhattan_dist = manhattan_distance(coordinates[0] - 1, coordinates[1])
            new_node = Node(manhattan_dist, current.g + 1, (coordinates[0] - 1, coordinates[1]))
            new_node.set_parent(current)
            fringe.put(new_node)

        if coordinates[1] - 1 >= 0 and my_map[coordinates[0]][coordinates[1] - 1] != '%':
            manhattan_dist = manhattan_distance(coordinates[0], coordinates[1] - 1)
            new_node = Node(manhattan_dist, current.g + 1, (coordinates[0], coordinates[1] - 1))
            new_node.set_parent(current)
            fringe.put(new_node)

        if coordinates[1] + 1 <= m - 1 and my_map[coordinates[0]][coordinates[1] + 1] != '%':
            manhattan_dist = manhattan_distance(coordinates[0], coordinates[1] + 1)
            new_node = Node(manhattan_dist, current.g + 1, (coordinates[0], coordinates[1] + 1))
            new_node.set_parent(current)
            fringe.put(new_node)

        if coordinates[0] + 1 <= n - 1 and my_map[coordinates[0] + 1][coordinates[1]] != '%':
            manhattan_dist = manhattan_distance(coordinates[0] + 1, coordinates[1])
            new_node = Node(manhattan_dist, current.g + 1, (coordinates[0] + 1, coordinates[1]))
            new_node.set_parent(current)
            fringe.put(new_node)


def manhattan_distance(x1, y1):
    return abs(x1 - goalX) + abs(y1 - goalY)


pacX, pacY = map(int, input().split())
goalX, goalY = map(int, input().split())
n, m = map(int, input().split())
myMap = []
for i in range(n):
    myMap.append(input())
for x in a_star_search(myMap, pacX, pacY):
    print(x[0], x[1])
