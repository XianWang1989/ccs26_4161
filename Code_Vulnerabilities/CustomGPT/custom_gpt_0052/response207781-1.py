
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
        open_set = set()     # Set of explorable nodes
        open_heap = []       # Priority queue for the lowest cost
        closed_set = set()   # Best path so far

        start_node = Node(0, current, self.manHatDist(current, end))
        open_set.add(start_node)
        heapq.heappush(open_heap, (start_node.cost, start_node))

        while open_heap:
            current_node = heapq.heappop(open_heap)[1]

            if current_node.pos == end:
                return self.getDirections(current_node)

            open_set.remove(current_node)
            closed_set.add(current_node)

            for tile in self.getAdjacentNodes(current_node.pos):
                if tile in closed_set:
                    continue

                tentative_cost = self.manHatDist(tile.pos, end) + current_node.cost + 1  # +1 for move cost
                if tile not in open_set or tentative_cost < tile.cost:
                    tile.cost = tentative_cost
                    tile.parent = current_node

                    if tile not in open_set:
                        open_set.add(tile)
                        heapq.heappush(open_heap, (tile.cost, tile))

        return []

    def getDirections(self, end_node):
        moves = []
        while end_node.parent is not None:
            moves.append(end_node.value)
            end_node = end_node.parent
        moves.reverse()
        return moves

    def getAdjacentNodes(self, curPos):
        all_moves = ['North', 'South', 'East', 'West']
        pos_moves = []
        for direction in all_moves:
            if self.canMove(direction, curPos):
                new_pos = self.getLocIfMove(curPos, direction)
                pos_moves.append(Node(direction, new_pos, 0))
        return pos_moves

    # Implement your heuristic functions below
    def manHatDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    # Placeholder methods
    def canMove(self, direction, pos):
        # Implement movement logic
        pass

    def getLocIfMove(self, pos, direction):
        # Implement logic for getting new position
        pass
