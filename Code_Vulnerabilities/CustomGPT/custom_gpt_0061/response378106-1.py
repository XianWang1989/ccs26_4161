
class FileHandler:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Get the current position
        t = self.f.tell()
        self.f.seek(0)  # Move to the start of the file
        lc = 0  # Line counter

        # Read through the file line by line
        while True:
            line = self.f.readline()  # Read a line
            if not line:  # End of file
                break
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        self.f.seek(t)  # Restore the original position
        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage
with FileHandler('example.txt') as fh:
    line_count = fh.tell()
    print(f"Number of lines before position: {line_count}")
