
def tell(self, char=False):
    t = self.f.tell()  # Get current position in bytes
    line_count = 0     # Line count

    # Move file pointer to the beginning to count lines
    self.f.seek(0)

    while True:
        line = self.f.readline()  # Read one line at a time
        if not line:  # Break if we've reached the end of the file
            break
        if t >= len(line):
            t -= len(line)
            line_count += 1
        else:
            break

    # Return either line count, or line count and remaining chars
    if char:
        return line_count, t
    return line_count

# Usage
with open('your_file.txt', 'a+') as f:
    editor = YourClass(f)  # Replace YourClass with the class name
    print(editor.tell())
