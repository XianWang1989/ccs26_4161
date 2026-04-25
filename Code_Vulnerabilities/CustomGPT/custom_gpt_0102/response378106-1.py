
def tell(self, char=False):
    t = self.f.tell()  # Get the current position
    self.f.seek(0)  # Go back to start of the file
    lc = 0  # Line counter
    chars_counted = 0  # Character counter if char=True

    for line in self.f:
        line_length = len(line)
        if t >= line_length + chars_counted:
            chars_counted += line_length
            lc += 1
        else:
            break

    self.f.seek(t)  # Return to the original position
    if char:
        return lc, t - chars_counted  # Return line count and character position
    return lc  # Just return the line count

# Example usage:
with open('example.txt', 'a+') as f:
    f.write("Hello\nWorld\nThis is a test.")
    position = f.tell()  # Save current position
    f.seek(0)  # Optionally reset to start for reading
    line_count = tell()  # Call your tell function
    print("Current line count:", line_count)
