
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Save the current position
        position = self.f.tell()
        # Move to the beginning of the file
        self.f.seek(0)

        # Read all lines into a list
        lines = self.f.readlines()
        lc = 0
        remaining = position

        for line in lines:
            if remaining >= len(line):
                remaining -= len(line)
                lc += 1
            else:
                break

        # Return the number of lines and remaining characters
        if char:
            return lc, remaining
        return lc

    def close(self):
        self.f.close()
