
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

class AStarSearch:
    def aStar(self, current, end):
        openSet = {}  # Node representation with cost
        openHeap = []  # Priority queue
        closedSet = set()

        curNode = Node("", current, self.manHatDist(current, end))
        openSet[current] = curNode
        heapq.heappush(openHeap, curNode)

        while openHeap:
            curNode = heapq.heappop(openHeap)
            if curNode.pos == end:
                return self.getDirections(curNode)

            closedSet.add(curNode.pos)
            del openSet[curNode.pos]

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue

                new_cost = curNode.cost + 1  # Assume movement cost is 1
                if tile.pos not in openSet or new_cost < openSet[tile.pos].cost:
                    tile.parent = curNode
                    tile.cost = new_cost + self.manHatDist(tile.pos, end)
                    openSet[tile.pos] = tile
                    heapq.heappush(openHeap, tile)

        return []

    def getDirections(self, endNode):
        moves = []
        tmpNode = endNode
        while tmpNode.parent is not None:
            moves.append(tmpNode.value)
            tmpNode = tmpNode.parent
        return moves[::-1]  # Reverse the moves to obtain the path 

    def getAdjacentNodes(self, curPos):
        allMoves = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in allMoves:
            if self.canMove(direction, curPos):
                movePos = self.getLocIfMove(curPos, direction)
                posMoves.append(Node(direction, movePos, 0))
        return posMoves

    def manHatDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    # Ensure these methods are correctly implemented
    def canMove(self, direction, curPos):
        # Define movement condition based on your grid limits
        pass

    def getLocIfMove(self, curPos, direction):
        # Map directions to their respective coordinate changes
        pass

# Usage example
a_star_search = AStarSearch()
start = (0, 0)
goal = (4, 4)
path = a_star_search.aStar(start, goal)
print("Path:", path)
