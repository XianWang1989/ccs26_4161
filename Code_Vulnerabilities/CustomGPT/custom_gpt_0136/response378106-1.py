
def tell(self, char=False):
    # Save the current position
    original_pos = self.f.tell()
    t, lc = original_pos, 0

    # Reset the file pointer to the beginning
    self.f.seek(0)

    # Read through the file line by line
    for line in self.f:
        if t >= len(line):
            t -= len(line)
            lc += 1
        else:
            break

    # Restore the original position
    self.f.seek(original_pos)

    if char:
        return lc, t
    return lc
