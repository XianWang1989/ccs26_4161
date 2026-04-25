
import heapq

class Node:
    def __init__(self, value, pos, cost, heuristic):
        self.pos = pos
        self.cost = cost
        self.heuristic = heuristic
        self.value = value
        self.parent = None

    def total_cost(self):
        return self.cost + self.heuristic

    def __lt__(self, other):
        return self.total_cost() < other.total_cost()

def aStar(self, current, end):
    openSet = []
    closedSet = {}
    start_node = Node(None, current, 0, self.manHatDist(current, end))
    heapq.heappush(openSet, start_node)
    closedSet[current] = start_node.cost

    while openSet:
        curNode = heapq.heappop(openSet)

        if curNode.pos == end:
            return self.getDirections(curNode)

        for tile in self.getAdjacentNodes(curNode.pos):
            new_cost = curNode.cost + 1  # Assuming uniform cost
            if tile.pos not in closedSet or new_cost < closedSet[tile.pos]:
                tile.parent = curNode
                tile.cost = new_cost
                tile.heuristic = self.manHatDist(tile.pos, end)

                if tile.pos not in closedSet:
                    closedSet[tile.pos] = new_cost
                    heapq.heappush(openSet, tile)

    return []

def getAdjacentNodes(self, curPos):
    directions = ['North', 'South', 'East', 'West']
    return [
        Node(direction, self.getLocIfMove(curPos, direction), 0, 0)
        for direction in directions if self.canMove(direction, curPos)
    ]
