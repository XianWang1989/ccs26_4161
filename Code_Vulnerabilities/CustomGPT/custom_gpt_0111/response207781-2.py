
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
        open_set = set()  # Explorable nodes
        open_heap = []    # All paths heap, with lowest cost on top
        closed_set = {}   # Best path so far with costs
        cur_node = Node(None, current, 0)
        open_set.add(cur_node)
        heapq.heappush(open_heap, (cur_node.cost, cur_node))

        while open_heap:
            cur_node = heapq.heappop(open_heap)[1]
            if cur_node.pos == end:
                return self.getDirections(cur_node)
            open_set.remove(cur_node)
            closed_set[cur_node.pos] = cur_node.cost

            for tile in self.getAdjacentNodes(cur_node.pos):
                if tile.pos in closed_set:
                    continue
                g_cost = cur_node.cost + 1  # Assuming uniform cost
                if tile.pos not in open_set or g_cost < closed_set.get(tile.pos, float('inf')):
                    tile.parent = cur_node
                    tile.cost = g_cost + self.manHatDist(tile.pos, end)
                    if tile.pos not in open_set:
                        open_set.add(tile)
                        heapq.heappush(open_heap, (tile.cost, tile))

        return []

    def getDirections(self, end_node):
        moves = []
        tmp_node = end_node
        while tmp_node.parent is not None:
            moves.append(tmp_node.value)
            tmp_node = tmp_node.parent
        moves.reverse()
        return moves

    # Include your getAdjacentNodes method and other utilities here
