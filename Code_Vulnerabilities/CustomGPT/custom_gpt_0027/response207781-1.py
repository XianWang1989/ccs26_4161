
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

class AStarPathfinder:
    def aStar(self, current, end):
        openHeap = []  # Priority queue
        closedSet = {}  # Dictionary to track visited nodes
        curNode = Node(None, current, self.manHatDist(current, end))

        heapq.heappush(openHeap, curNode)

        while openHeap:
            curNode = heapq.heappop(openHeap)

            if curNode.pos == end:
                return self.getDirections(curNode)

            closedSet[curNode.pos] = curNode.cost

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue
                new_cost = curNode.cost + self.euclidDist(curNode.pos, tile.pos)

                if tile.pos not in [node.pos for node in openHeap]:
                    tile.cost = new_cost + self.manHatDist(tile.pos, end)
                    tile.parent = curNode
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

    # Assume manHatDist and euclidDist are defined elsewhere
