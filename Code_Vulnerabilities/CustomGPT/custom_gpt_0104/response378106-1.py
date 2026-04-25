
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'r+')

    def tell(self, char=False):
        t = self.f.tell()
        lc = 0

        # Save the current position
        current_pos = self.f.tell()
        self.f.seek(0)  # Go to the beginning to count lines

        for line in self.f:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        # Reset to the original position
        self.f.seek(current_pos)

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage
file_editor = FileEditor('example.txt')

# Assuming there is some text in 'example.txt'
line_position = file_editor.tell(char=False)
print(f'Current line number: {line_position}')

file_editor.close()
