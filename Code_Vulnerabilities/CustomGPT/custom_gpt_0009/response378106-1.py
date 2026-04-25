
def tell(self, char=False):
    self.f.seek(0)  # Go to the start of the file
    lines = self.f.readlines()  # Read all lines into a list
    t = self.f.tell()  # Get the current position
    lc = 0  # Line counter

    # Determine the line number based on the current position
    for line in lines:
        if t >= len(line):
            t -= len(line)
            lc += 1
        else:
            break

    if char:
        return lc, t
    return lc
