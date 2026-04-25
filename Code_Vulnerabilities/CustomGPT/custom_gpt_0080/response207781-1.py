
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

# Perform an A* search to find the best path to the target position
def aStar(self, current, end):
    open_set = {}
    open_heap = []
    closed_set = set()

    start_node = Node(None, current, self.manHatDist(current, end))
    open_set[current] = start_node
    heapq.heappush(open_heap, start_node)

    while open_heap:
        cur_node = heapq.heappop(open_heap)

        if cur_node.pos == end:
            return self.getDirections(cur_node)

        del open_set[cur_node.pos]
        closed_set.add(cur_node.pos)

        for tile in self.getAdjacentNodes(cur_node.pos):
            if tile.pos in closed_set:
                continue

            tile.parent = cur_node
            tile.cost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current)

            if tile.pos not in open_set or tile.cost < open_set[tile.pos].cost:
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
