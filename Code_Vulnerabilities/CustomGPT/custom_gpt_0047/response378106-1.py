
def tell(self, char=False):
    # Get the current position in the file
    t = self.f.tell()

    # Seek to the beginning of the file
    self.f.seek(0)

    # Read all lines at once
    lines = self.f.readlines()

    lc = 0  # Line count
    for line in lines:
        if t >= len(line):  # Check if current position is beyond this line
            t -= len(line)
            lc += 1
        else:
            break

    # Return the result based on char flag
    if char:
        return lc, t
    return lc

# Example usage:
with open('example.txt', 'a+') as f:
    f.write("First line\nSecond line\nThird line\n")
    f.seek(0)  # Go back to start for demonstration
    position = f.tell()  # Example position to check
    line_count = tell(f)
    print(f"Current line count: {line_count}")
