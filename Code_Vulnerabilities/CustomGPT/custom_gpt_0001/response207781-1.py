
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

class Pathfinder:
    def aStar(self, current, end):
        openSet = set()  # Set of explorable nodes
        openHeap = []    # Min-heap for node costs
        curNode = Node('', current, self.manHatDist(current, end))
        openSet.add(current)
        heapq.heappush(openHeap, (curNode.cost, curNode))

        while openHeap:
            curNode = heapq.heappop(openHeap)[1]

            if curNode.pos == end:
                return self.getDirections(curNode)

            openSet.remove(curNode.pos)  # Update based on positional ownership

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos not in openSet:  # Check openSet by position
                    tile.parent = curNode
                    tile.cost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current)
                    openSet.add(tile.pos)  # Track positions only
                    heapq.heappush(openHeap, (tile.cost, tile))
                else:
                    # If it's already been visited but with a higher cost, update it
                    for existing in openHeap:
                        if existing[1].pos == tile.pos and existing[1].cost > tile.cost:
                            existing[1].cost = tile.cost  # Update cost
                            # You may need to re-heapify here
                            heapq.heapify(openHeap)
                            break

        return []

    def getDirections(self, endNode):
        moves = []
        tmpNode = endNode
        while tmpNode.parent is not None:
            moves.append(tmpNode.value)
            tmpNode = tmpNode.parent
        moves.reverse()
        return moves

    # Placeholder for distance calculation functions
    def manHatDist(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def euclidDist(self, a, b):
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

    # Replace with your actual implementation
    def getAdjacentNodes(self, curPos):
        allMoves = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in allMoves:
            if self.canMove(direction, curPos):
                posMoves.append(Node(direction, self.getLocIfMove(curPos, direction), 0))
        return posMoves
