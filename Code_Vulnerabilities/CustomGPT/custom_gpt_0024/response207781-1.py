
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

class AStar:
    def aStar(self, current, end):
        openSet = {}  # Dictionary to hold nodes
        openHeap = []  # Priority queue for the heap
        closedSet = set()  # Best path tracking

        startNode = Node("", current, self.manHatDist(current, end))
        openSet[current] = startNode
        heapq.heappush(openHeap, startNode)

        while openHeap:
            curNode = heapq.heappop(openHeap)

            if curNode.pos == end:
                return self.getDirections(curNode)

            closedSet.add(curNode.pos)
            del openSet[curNode.pos]

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue

                # Update costs and parents
                tile.parent = curNode
                tile.cost = curNode.cost + self.manHatDist(tile.pos, end)

                if tile.pos not in openSet:
                    openSet[tile.pos] = tile
                    heapq.heappush(openHeap, tile)
                else:
                    existingNode = openSet[tile.pos]
                    if tile.cost < existingNode.cost:
                        existingNode.parent = curNode
                        existingNode.cost = tile.cost
                        # Reorder heap, because cost is updated
                        heapq.heapify(openHeap)

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
        # Implementation of getting adjacent nodes
        pass

    def manHatDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
