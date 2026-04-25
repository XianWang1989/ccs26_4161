
def tell(self, char=False):
    # Store the current position
    t = self.f.tell()
    self.f.seek(0)  # Move to the beginning of the file
    lines = self.f.readlines()  # Read all lines into a list
    lc = 0  # Line counter

    # Iterate through the lines to find the corresponding line number
    for line in lines:
        if t >= len(line):
            t -= len(line)
            lc += 1
        else:
            break

    # Return the line count and remaining character position if needed
    if char:
        return lc, t
    return lc
