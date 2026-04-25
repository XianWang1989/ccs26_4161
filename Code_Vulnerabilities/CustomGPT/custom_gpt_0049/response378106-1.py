
def tell(self, char=False):
    t = self.f.tell()  # Get the current position in bytes
    self.f.seek(0)     # Move to the beginning of the file
    lines = self.f.readlines()  # Read all lines into a list
    lc = 0  # Line counter

    for line in lines:
        if t >= len(line):
            t -= len(line)  # Subtract line length from the position
            lc += 1
        else:
            break

    self.f.seek(t)  # Restore the original position
    if char:
        return lc, t
    return lc
