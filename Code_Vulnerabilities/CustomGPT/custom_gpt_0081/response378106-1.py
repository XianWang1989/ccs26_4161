
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Get the current position
        t = self.f.tell()

        # Go back to the start of the file and read all lines
        self.f.seek(0)
        lines = self.f.readlines()  # Read all lines into a list

        lc = 0  # Line count
        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Return either line count or line count with remaining characters
        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage
file_editor = FileEditor('example.txt')
# Let's say you write something to your file first
with open('example.txt', 'a') as f:
    f.write("First line\nSecond line\nThird line\n")

# Use the tell method
line_count = file_editor.tell()
print(f"Number of lines to current position: {line_count}")

# Close the file when done
file_editor.close()
