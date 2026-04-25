
import heapq

class Node:
    def __init__(self, value, pos, cost, parent=None):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost

class PathFinder:
    def __init__(self):
        # Initialize if needed, e.g., to store the grid or other configurations
        pass

    def manHatDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def euclidDist(self, pos1, pos2):
        return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5

    def getAdjacentNodes(self, curPos):
        allMoves = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in allMoves:
            if self.canMove(direction, curPos):
                newPos = self.getLocIfMove(curPos, direction)
                posMoves.append(Node(direction, newPos, 0))
        return posMoves

    def aStar(self, current, end):
        openSet = {}
        openHeap = []
        closedSet = set()

        startNode = Node('', current, 0 + self.manHatDist(current, end))
        openSet[startNode.pos] = startNode
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

                new_cost = curNode.cost + 1  # Assuming movement cost is uniform
                heuristic = self.manHatDist(tile.pos, end)
                total_cost = new_cost + heuristic

                if tile.pos not in openSet or total_cost < openSet[tile.pos].cost:
                    tile.cost = total_cost
                    tile.parent = curNode

                    if tile.pos not in openSet:
                        openSet[tile.pos] = tile
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
