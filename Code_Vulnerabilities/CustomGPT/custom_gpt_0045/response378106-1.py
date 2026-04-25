
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Get the current byte position
        current_position = self.f.tell()

        # Go back to the beginning of the file and read the lines
        self.f.seek(0)
        lines = self.f.readlines()

        lc = 0
        for line in lines:
            if current_position >= len(line):
                current_position -= len(line)
                lc += 1
            else:
                break

        if char:
            return lc, current_position
        return lc

    def close(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')
print("Line Number:", editor.tell())  # Get the line number of the current position
editor.close()
