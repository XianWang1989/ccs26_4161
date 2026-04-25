
def tell(self, char=False):
    current_pos = self.f.tell()
    self.f.seek(0)  # Move to the start of the file
    lines = self.f.readlines()  # Read all lines into a list
    self.f.seek(current_pos)  # Move back to the original position

    line_count = 0
    char_count = 0

    for line in lines:
        if current_pos >= char_count + len(line):
            char_count += len(line)
            line_count += 1
        else:
            break

    if char:
        return line_count, current_pos - char_count
    return line_count
