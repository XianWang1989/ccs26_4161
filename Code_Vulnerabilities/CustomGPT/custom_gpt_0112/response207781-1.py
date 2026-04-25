
import heapq

# Node class for A* search
class Node:
    def __init__(self, value, pos, path_cost, heuristic_cost):
        self.pos = pos
        self.path_cost = path_cost
        self.heuristic_cost = heuristic_cost
        self.value = value
        self.parent = None

    @property
    def cost(self):
        return self.path_cost + self.heuristic_cost

    def __lt__(self, other):
        return self.cost < other.cost

# A* search algorithm
def aStar(self, current, end):
    open_set = {}  # Dictionary for open set
    open_heap = []  # List for the heap
    closed_set = set()  # Set for closed nodes

    start_node = Node("", current, 0, self.manHatDist(current, end))
    open_set[current] = start_node
    heapq.heappush(open_heap, start_node)

    while open_heap:
        cur_node = heapq.heappop(open_heap)

        if cur_node.pos == end:
            return self.getDirections(cur_node)

        open_set.pop(cur_node.pos, None)  # Remove from open set
        closed_set.add(cur_node.pos)  # Add to closed set

        for tile in self.getAdjacentNodes(cur_node.pos):
            if tile.pos not in closed_set:
                new_cost = cur_node.path_cost + 1  # Assume all moves cost 1
                tile.parent = cur_node
                tile.path_cost = new_cost
                tile.heuristic_cost = self.manHatDist(tile.pos, end)

                if tile.pos not in open_set or new_cost < open_set[tile.pos].path_cost:
                    open_set[tile.pos] = tile
                    heapq.heappush(open_heap, tile)

    return []

# Get the moves made to get to this endNode
def getDirections(self, endNode):
    moves = []
    tmpNode = endNode

    while tmpNode.parent is not None:
        moves.append(tmpNode.value)
        tmpNode = tmpNode.parent

    moves.reverse()
    return moves

# Get adjacent nodes method to be defined as-is
