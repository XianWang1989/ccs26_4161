
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Save the current position of the file pointer
        current_position = self.f.tell()

        # Seek to the beginning of the file to read lines
        self.f.seek(0)

        # Read all lines at once
        lines = self.f.readlines()

        # Calculate the line number based on current position
        line_count = 0
        pos_in_line = current_position

        for line in lines:
            if pos_in_line >= len(line):
                pos_in_line -= len(line)
                line_count += 1
            else:
                break

        # Restore the file pointer to the previous position
        self.f.seek(current_position)

        if char:
            return line_count, pos_in_line
        return line_count

    def close(self):
        # Don't forget to close the file
        self.f.close()

# Example of usage
editor = FileEditor("example.txt")
# Assuming the file contains several lines of text
line_number = editor.tell()
print(f"Current line number: {line_number}")
editor.close()
