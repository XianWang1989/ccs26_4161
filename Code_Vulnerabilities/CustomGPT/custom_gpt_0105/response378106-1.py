
def tell(self, char=False):
    current_pos = self.f.tell()  # Save the current position
    line_count = 0
    self.f.seek(0)  # Go to the start of the file

    for line in self.f:
        if current_pos >= len(line):
            current_pos -= len(line)
            line_count += 1
        else:
            break

    self.f.seek(current_pos)  # Restore the file position
    if char:
        return line_count, current_pos
    return line_count
