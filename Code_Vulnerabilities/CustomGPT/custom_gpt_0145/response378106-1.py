
def tell(self, char=False):
    # Save the current position
    original_position = self.f.tell()

    # Reset to the beginning to calculate line number
    self.f.seek(0)

    t, lc = original_position, 0

    for line in self.f:
        if t >= len(line):
            t -= len(line)
            lc += 1
        else:
            break

    # Restore the original position of the file pointer
    self.f.seek(original_position)

    if char:
        return lc, t
    return lc
