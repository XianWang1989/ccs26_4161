
import heapq

class Node:
    def __init__(self, value, pos, g_cost, h_cost):
        self.pos = pos
        self.g_cost = g_cost  # Cost from start to node
        self.h_cost = h_cost  # Heuristic cost to end
        self.cost = g_cost + h_cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Simplified comparison

class PathFinder:
    def aStar(self, current, end):
        openHeap = []  # Priority queue for A* search
        closedSet = {}  # Using a dictionary for fast lookups
        start_node = Node('', current, 0, self.manHatDist(current, end))
        heapq.heappush(openHeap, start_node)

        while openHeap:
            curNode = heapq.heappop(openHeap)

            if curNode.pos == end:
                return self.getDirections(curNode)

            closedSet[curNode.pos] = curNode

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue

                g_cost = curNode.g_cost + 1  # Assuming uniform cost for each move
                tile.g_cost = g_cost
                tile.h_cost = self.manHatDist(tile.pos, end)
                tile.cost = g_cost + tile.h_cost
                tile.parent = curNode

                if not any(open_node.pos == tile.pos and open_node.g_cost <= g_cost for open_node in openHeap):
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
                newPos = self.getLocIfMove(curPos, direction)
                posMoves.append(Node(direction, newPos, 0, 0))  # g_cost will be calculated later
        return posMoves
