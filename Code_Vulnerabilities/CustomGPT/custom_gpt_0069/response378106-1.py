
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Save the current position
        t = self.f.tell()
        self.f.seek(0)

        # Read all lines into a list
        lines = self.f.readlines()

        lc = 0  # line counter
        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        self.f.seek(t)  # Reset to original position
        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage
with FileEditor('example.txt') as editor:
    print("Current line position:", editor.tell())
