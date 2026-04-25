
def tell(self, char=False):
    # Store the current position
    t = self.f.tell()

    # Move to the beginning to read the lines
    self.f.seek(0)

    # Read all lines into memory
    lines = self.f.readlines()

    # Calculate line and position
    lc = 0
    for line in lines:
        if t >= len(line):
            t -= len(line)
            lc += 1
        else:
            break

    # Return the result based on char parameter
    if char:
        return lc, t
    return lc
