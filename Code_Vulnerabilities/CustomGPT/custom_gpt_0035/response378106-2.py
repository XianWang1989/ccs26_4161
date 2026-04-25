
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        self.f.seek(0)  # Ensure we start reading from the beginning
        lines = self.f.readlines()

        t = self.f.tell()  # Get the current byte position
        lc = 0  # Line count

        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        if char:
            return lc, t
        return lc

# Example usage
with FileEditor('example.txt') as editor:
    line_count = editor.tell()
    print(f"Current line: {line_count}")
