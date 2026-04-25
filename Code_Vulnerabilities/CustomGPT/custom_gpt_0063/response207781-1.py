
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        # Comparison for priority queue (min-heap)
        return self.cost < other.cost

class AStarAlgorithm:
    def __init__(self):
        self.closed_set = {}
        self.open_heap = []

    def manHatDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def aStar(self, current, end):
        start_node = Node(None, current, 0)
        start_node.cost = self.manHatDist(current, end)
        heapq.heappush(self.open_heap, (start_node.cost, start_node))
        self.closed_set[current] = start_node.cost

        while self.open_heap:
            cur_node = heapq.heappop(self.open_heap)[1]

            if cur_node.pos == end:
                return self.getDirections(cur_node)

            for tile in self.getAdjacentNodes(cur_node.pos):
                new_cost = cur_node.cost + 1  # Assuming cost between nodes is uniform

                if tile.pos not in self.closed_set or new_cost < self.closed_set[tile.pos]:
                    tile.parent = cur_node
                    tile.cost = new_cost + self.manHatDist(tile.pos, end)
                    self.closed_set[tile.pos] = new_cost
                    heapq.heappush(self.open_heap, (tile.cost, tile))

        return []

    def getDirections(self, endNode):
        moves = []
        tmpNode = endNode
        while tmpNode.parent is not None:
            moves.append(tmpNode.value)
            tmpNode = tmpNode.parent
        return moves[::-1]  # Reverse the list

    def getAdjacentNodes(self, curPos):
        allMoves = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in allMoves:
            if self.canMove(direction, curPos):  # Assumes this method is implemented elsewhere
                new_pos = self.getLocIfMove(curPos, direction)  # Assumes this method is implemented
                posMoves.append(Node(direction, new_pos, 0))
        return posMoves
