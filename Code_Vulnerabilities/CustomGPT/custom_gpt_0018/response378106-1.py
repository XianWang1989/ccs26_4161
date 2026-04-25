
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Store the current file position
        current_position = self.f.tell()

        # Retrieve all lines from the file
        self.f.seek(0)  # Move to the beginning of the file
        lines = self.f.readlines()  # Read all lines into memory

        lc, char_offset = 0, 0

        # Calculate line count and character offset
        for line in lines:
            line_length = len(line)
            if char_offset + line_length > current_position:
                break
            char_offset += line_length
            lc += 1

        # Reset cursor back to the original position
        self.f.seek(current_position)

        if char:
            return lc, current_position - char_offset
        return lc

    def close(self):
        self.f.close()

# Usage Example
if __name__ == "__main__":
    editor = FileEditor('example.txt')

    # Append some text for demonstration
    editor.f.write("First line\nSecond line\nThird line\n")
    editor.f.flush()  # Ensure data is written to the file

    # Testing the `tell` function
    line_count = editor.tell()
    print(f'Total lines: {line_count}')

    # Close the file
    editor.close()
