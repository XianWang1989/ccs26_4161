
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
        openHeap = []
        closedSet = set()

        start_node = Node(None, current, self.manHatDist(current, end))
        heapq.heappush(openHeap, (start_node.cost, start_node))

        while openHeap:
            curNode = heapq.heappop(openHeap)[1]
            if curNode.pos == end:
                return self.getDirections(curNode)

            closedSet.add(curNode.pos)
            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue

                tile.cost = self.manHatDist(tile.pos, end) + curNode.cost + 1  # Adding step cost
                tile.parent = curNode

                # Check if this node is already in the heap
                if not any(t.pos == tile.pos and t.cost <= tile.cost for _, t in openHeap):
                    heapq.heappush(openHeap, (tile.cost, tile))

        return []

    def getDirections(self, endNode):
        moves = []
        while endNode.parent is not None:
            moves.append(endNode.value)
            endNode = endNode.parent
        return moves[::-1]

    def getAdjacentNodes(self, curPos):
        # Your existing implementation
        ...

    def manHatDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

# Ensure to update canMove and getLocIfMove methods accordingly
