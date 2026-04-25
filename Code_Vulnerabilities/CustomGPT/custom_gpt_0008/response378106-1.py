
def tell(self, char=False):
    current_pos = self.f.tell()  # Store the current position
    self.f.seek(0)  # Seek to the beginning of the file
    lc = 0  # Line count

    # Read through the file until reaching the saved position
    for line in self.f:
        if current_pos >= len(line):
            current_pos -= len(line)
            lc += 1
        else:
            break

    self.f.seek(current_pos)  # Reset to the original position

    if char:
        return lc, current_pos
    return lc
