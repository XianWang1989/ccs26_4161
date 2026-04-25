
def tell(self, char=False):
    current_position = self.f.tell()  # Save current position
    line_count = 0

    self.f.seek(0)  # Go to the start of the file
    for line in self.f:
        line_length = len(line)
        if current_position >= line_length:
            current_position -= line_length
            line_count += 1
        else:
            break

    self.f.seek(current_position)  # Restore the file pointer to its original position

    if char:
        return line_count, current_position
    return line_count
