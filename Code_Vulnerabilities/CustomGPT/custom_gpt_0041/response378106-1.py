
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Get the current file position
        current_position = self.f.tell()

        # Read the entire file into a list of lines
        self.f.seek(0)  # Go to the start of the file
        lines = self.f.readlines()

        # Calculate the line count and the character position
        line_count = 0
        byte_count = current_position

        for line in lines:
            line_length = len(line)
            if byte_count >= line_length:
                byte_count -= line_length
                line_count += 1
            else:
                break

        if char:
            return line_count, byte_count
        return line_count

    def close(self):
        self.f.close()

# Usage example
editor = FileEditor('example.txt')
line_num = editor.tell()  # Get the line number
print(f'Current line number: {line_num}')
editor.close()
