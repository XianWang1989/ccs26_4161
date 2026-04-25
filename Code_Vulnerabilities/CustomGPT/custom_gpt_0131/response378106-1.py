
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Fetch the current position in the file
        t = self.f.tell()

        # Seek to the beginning and read all lines at once
        self.f.seek(0)
        lines = self.f.readlines()  # This stores all lines in memory

        # Initialize line count
        lc = 0 

        # Calculate the line number
        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Return character or line count as needed
        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')
# Write something to demonstrate the tell function with a few lines
editor.f.write("Hello, World!\nThis is a test file.\nThis line is for testing.")
editor.f.flush()  # Ensure the written content is visible

# Getting the line number of the current position
line_count = editor.tell()
print(f'Current line count: {line_count}')  # Expected output could vary based on the content
editor.close()
