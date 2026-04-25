
import heapq  # Ensure you import heapq for priority queue functionality

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
        open_set = {}  # Node reference as {Node Object: Cost}
        open_heap = []  # Min-heap based on cost
        closed_set = set()  # Explored nodes

        start_node = Node(0, current, self.manHatDist(current, end))
        open_set[start_node] = start_node.cost
        heapq.heappush(open_heap, start_node)

        while open_heap:
            cur_node = heapq.heappop(open_heap)

            if cur_node.pos == end:
                return self.getDirections(cur_node)

            closed_set.add(cur_node.pos)

            for tile in self.getAdjacentNodes(cur_node.pos):
                if tile.pos in closed_set:
                    continue

                new_cost = cur_node.cost + self.euclidDist(cur_node.pos, tile.pos)

                if tile not in open_set or new_cost < open_set[tile]:
                    tile.parent = cur_node
                    tile.cost = new_cost + self.manHatDist(tile.pos, end)

                    open_set[tile] = tile.cost  # Update or add the cost
                    heapq.heappush(open_heap, tile)

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
                if new_pos not in posMoves:  # Ensure unique positions
                    posMoves.append(Node(direction, new_pos, 0))
        return posMoves

    # Stub methods for distance calculations
    def manHatDist(self, pos1, pos2):
        # Implement Manhattan distance calculation
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def euclidDist(self, pos1, pos2):
        # Implement Euclidian distance calculation
        return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5

    def canMove(self, direction, curPos):
        # Implement movement checking logic
        pass

    def getLocIfMove(self, curPos, direction):
        # Implement logic to compute new position based on movement direction
        pass
