
def tell(self, char=False):
    # Move the file pointer to the beginning
    self.f.seek(0)
    lines = self.f.readlines()  # Read all lines into a list
    t = self.f.tell()  # Current position
    lc = 0  # Line count

    # Iterate over the lines to determine the line number
    for line in lines:
        if t >= len(line):
            t -= len(line)
            lc += 1
        else:
            break

    if char:
        return lc, t
    return lc
