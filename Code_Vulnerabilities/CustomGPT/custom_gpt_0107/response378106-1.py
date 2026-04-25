
def tell(self, char=False):
    t = self.f.tell()
    self.f.seek(0)

    # Read all lines into a list
    lines = self.f.readlines()

    lc = 0
    for line in lines:
        if t >= len(line):
            t -= len(line)
            lc += 1
        else:
            break

    self.f.seek(t)  # Reset the position of the file pointer
    if char:
        return lc, t
    return lc
