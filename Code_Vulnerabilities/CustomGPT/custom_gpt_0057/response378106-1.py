
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        filename = self.file
        t = self.f.tell()
        self.f.seek(0)
        lines = self.f.readlines()
        lc = 0
        position = t
        for line in lines:
            if position >= len(line):
                position -= len(line)
                lc += 1
            else:
                break
        self.f.seek(t)  # Return to the original position after calculating
        if char:
            return lc, position
        return lc

    def close(self):
        self.f.close()

# Example usage
file_editor = FileEditor('example.txt')
line_count = file_editor.tell()
print(f"Current line number: {line_count}")
file_editor.close()
