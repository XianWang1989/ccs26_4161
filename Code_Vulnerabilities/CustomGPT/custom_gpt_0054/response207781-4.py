
def getAdjacentNodes(self, curPos):
    directions = {
        'North': (0, 1),
        'South': (0, -1),
        'East': (1, 0),
        'West': (-1, 0)
    }
    posMoves = []
    for direction, delta in directions.items():
        nextPos = (curPos[0] + delta[0], curPos[1] + delta[1])
        if self.canMove(direction, curPos):  # Ensure movement logic is efficient
            posMoves.append(Node(direction, nextPos, 0))
    return posMoves
