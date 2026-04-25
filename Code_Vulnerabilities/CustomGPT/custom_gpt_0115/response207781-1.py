
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

    def __hash__(self):
        return hash(self.pos)

    def __eq__(self, other):
        return self.pos == other.pos

class YourClass:
    def aStar(self, current, end):
        openSet = {}  # Change to a dictionary for O(1) access
        openHeap = []
        closedSet = set()

        start_node = Node(None, current, self.manHatDist(current, end))
        openSet[start_node] = start_node.cost
        heapq.heappush(openHeap, start_node)

        while openHeap:
            curNode = heapq.heappop(openHeap)

            if curNode.pos == end:
                return self.getDirections(curNode)

            closedSet.add(curNode)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile in closedSet:
                    continue

                new_cost = curNode.cost + 1 + self.manHatDist(tile.pos, end)
                if tile in openSet:
                    if new_cost < openSet[tile]:
                        tile.parent = curNode
                        tile.cost = new_cost
                        openSet[tile] = new_cost
                        heapq.heappush(openHeap, tile)
                else:
                    tile.parent = curNode
                    tile.cost = new_cost
                    openSet[tile] = new_cost
                    heapq.heappush(openHeap, tile)

        return []

    def getDirections(self, endNode):
        moves = []
        tmpNode = endNode
        while tmpNode.parent is not None:
            moves.append(tmpNode.value)
            tmpNode = tmpNode.parent
        moves.reverse()
        return moves

    def getAdjacentNodes(self, curPos):
        allMoves = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in allMoves:
            if self.canMove(direction, curPos):
                new_pos = self.getLocIfMove(curPos, direction)
                posMoves.append(Node(direction, new_pos, 0))
        return posMoves

    # Add your heuristic functions, canMove, getLocIfMove methods
