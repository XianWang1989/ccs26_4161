
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Get the current position
        t = self.f.tell()
        # Move to the beginning of the file
        self.f.seek(0)
        lines = self.f.readlines()

        lc = 0  # Line count
        # Determine the line number based on the position
        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Return result based on 'char' parameter
        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()
