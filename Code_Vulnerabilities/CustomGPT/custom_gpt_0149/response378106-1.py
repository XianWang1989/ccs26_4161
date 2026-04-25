
class MyFileHandler:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()  # Get current position
        self.f.seek(0)  # Go to the beginning of the file
        lc = 0  # Line count

        while True:
            line = self.f.readline()  # Read line by line
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
with MyFileHandler('example.txt') as handler:
    line_count = handler.tell()
    print(f"Line count: {line_count}")
