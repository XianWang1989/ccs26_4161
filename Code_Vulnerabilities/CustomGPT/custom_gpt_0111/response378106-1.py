
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Save the current position
        current_pos = self.f.tell()
        line_count = 0
        self.f.seek(0)

        # Read lines into a list
        lines = self.f.readlines()

        # Calculate the line and character position
        for line in lines:
            if current_pos >= len(line):
                current_pos -= len(line)
                line_count += 1
            else:
                break

        if char:
            return line_count, current_pos
        return line_count

    def close(self):
        self.f.close()

# Usage
editor = FileEditor('example.txt')
line_position = editor.tell(char=False)
print('Line Position:', line_position)
editor.close()
