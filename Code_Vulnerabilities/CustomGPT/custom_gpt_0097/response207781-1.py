
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
        open_set = set()
        open_heap = []
        closed_set = set()
        start_node = Node(0, current, self.manHatDist(current, end))
        open_set.add(start_node)
        heapq.heappush(open_heap, start_node)

        while open_heap:
            cur_node = heapq.heappop(open_heap)

            if cur_node.pos == end:
                return self.getDirections(cur_node)

            open_set.remove(cur_node)
            closed_set.add(cur_node)

            for tile in self.getAdjacentNodes(cur_node.pos):
                if tile in closed_set:
                    continue

                tentative_cost = cur_node.cost + self.euclidDist(cur_node.pos, tile.pos)
                if tile not in open_set or tentative_cost < tile.cost:
                    tile.parent = cur_node
                    tile.cost = tentative_cost + self.manHatDist(tile.pos, end)

                    if tile not in open_set:
                        open_set.add(tile)
                        heapq.heappush(open_heap, tile)

        return []

    def getDirections(self, endNode):
        moves = []
        tmpNode = endNode
        while tmpNode.parent is not None:
            moves.append(tmpNode.value)
            tmpNode = tmpNode.parent
        return moves[::-1]  # Reverse the list in one step

    def getAdjacentNodes(self, curPos):
        allMoves = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in allMoves:
            if self.canMove(direction, curPos):
                posMoves.append(Node(direction, self.getLocIfMove(curPos, direction), 0))
        return posMoves

    # Define your manHatDist and euclidDist methods below
