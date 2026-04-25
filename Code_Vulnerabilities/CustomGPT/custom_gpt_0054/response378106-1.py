
def tell(self, char=False):
    t, lc = self.f.tell(), 0
    self.f.seek(0)  # Move back to the start of the file
    lines = self.f.readlines()  # Read all lines into a list
    for line in lines:
        if t >= len(line):
            t -= len(line)
            lc += 1
        else:
            break
    if char:
        return lc, t
    return lc
