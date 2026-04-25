
def tell(self, char=False):
    self.f.seek(0)  # Go to the start of the file
    lines = self.f.readlines()  # Read all lines into memory
    t = self.f.tell()  # Get the current position (in bytes)

    lc = 0  # Line count
    current_pos = 0  # Keep track of the byte position

    for line in lines:
        if current_pos + len(line) > t:
            break
        current_pos += len(line)
        lc += 1

    if char:
        return lc, t
    return lc
