
def tell(self, char=False):
    current_position = self.f.tell()
    line_count = 0
    self.f.seek(0)

    while True:
        line = self.f.readline()
        if not line:
            break
        if current_position >= len(line):
            current_position -= len(line)
            line_count += 1
        else:
            break

    self.f.seek(current_position)  # Restore the original position

    if char:
        return line_count, current_position
    return line_count
