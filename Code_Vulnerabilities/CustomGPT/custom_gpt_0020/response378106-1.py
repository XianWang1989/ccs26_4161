
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()  # Get the current position
        self.f.seek(0)     # Move to the beginning of the file

        # Read all lines into a list
        lines = self.f.readlines()
        lc = 0  # Line count

        for line in lines:
            if t >= len(line):
                t -= len(line)  # Deduct the line length from position
                lc += 1         # Increment line count
            else:
                break

        self.f.seek(t)  # Restore the file to its original position
        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()


# Example usage
filename = 'example.txt'
editor = FileEditor(filename)

# Assume we append some text to the file
editor.f.write("Hello, World!\n")
editor.f.write("This is line 2.\n")
editor.f.write("And this is line 3.\n")
editor.f.flush()  # Ensure data is written to disk

# Now use tell function
position = editor.tell()
print(f"Current line count: {position}")

# Clean up
editor.close()
