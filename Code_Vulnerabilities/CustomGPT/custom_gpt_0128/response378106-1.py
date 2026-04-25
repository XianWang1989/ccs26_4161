
def tell(self, char=False):
    t = self.f.tell()
    self.f.seek(0)
    lc = 0
    while True:
        line = self.f.readline()
        if not line:  # End of file
            break
        if t >= len(line):
            t -= len(line)
            lc += 1
        else:
            break
    self.f.seek(t + len(line))  # Reset to where we left off
    if char:
        return lc, t
    return lc
