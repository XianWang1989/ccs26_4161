
def tell(self, char=False):
    # Store the current position
    current_pos = self.f.tell()

    # Reset to the beginning of the file
    self.f.seek(0)

    line_count = 0
    remaining = current_pos

    for line in self.f:
        if remaining >= len(line):
            remaining -= len(line)
            line_count += 1
        else:
            break

    # Restore the original position
    self.f.seek(current_pos)

    if char:
        return line_count, remaining
    return line_count
