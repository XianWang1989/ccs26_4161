
def tell(self, char=False):
    t = self.f.tell()  # Get the current position
    self.f.seek(0)     # Rewind the file to the beginning
    lines = self.f.readlines()  # Read all lines into a list
    lc = 0  # Line count

    for line in lines:
        if t >= len(line):
            t -= len(line)
            lc += 1
        else:
            break

    if char:
        return lc, t
    return lc
