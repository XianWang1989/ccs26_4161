
def tell(self, char=False):
    # Store the current position
    current_position = self.f.tell()
    line_count = 0

    # Move to the beginning to count lines
    self.f.seek(0)

    for line in self.f:
        # If we have traversed enough bytes, stop
        if current_position >= len(line):
            current_position -= len(line)
            line_count += 1
        else:
            break

    # Restore original position
    self.f.seek(current_position)

    if char:
        return line_count, current_position
    return line_count
