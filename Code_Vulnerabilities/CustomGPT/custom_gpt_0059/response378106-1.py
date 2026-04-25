
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        current_position = self.f.tell()
        self.f.seek(0)

        # Read all lines into a list
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
print(editor.tell())  # Output the line number
editor.close()
