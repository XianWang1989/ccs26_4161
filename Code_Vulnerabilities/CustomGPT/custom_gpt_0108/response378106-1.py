
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Save the current position
        current_pos = self.f.tell()
        # Move to the beginning to read lines
        self.f.seek(0)

        # Read all lines into memory
        lines = self.f.readlines()
        lc = len(lines)  # Line count

        # Calculate line number and character offset
        line_number = 0
        char_offset = current_pos

        for line in lines:
            if char_offset >= len(line):
                char_offset -= len(line)
                line_number += 1
            else:
                break

        # Return the position based on user's request
        if char:
            return line_number, char_offset
        return line_number

    def close(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')
print(editor.tell())  # Get line number
print(editor.tell(char=True))  # Get line number and character offset
editor.close()
