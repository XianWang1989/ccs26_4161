
class FileManager:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        pos = self.f.tell()
        self.f.seek(0)  # Reset to the beginning
        lines = self.f.readlines()  # Read all lines into a list

        line_count = 0
        char_count = pos  # Start from current position

        for line in lines:
            if char_count >= len(line):
                char_count -= len(line)
                line_count += 1
            else:
                break

        self.f.seek(pos)  # Restore the original position

        if char:
            return line_count, char_count
        return line_count

    def close(self):
        self.f.close()

# Usage example
with FileManager('example.txt') as fm:
    print(fm.tell())  # Get the line count
