
import docx
import sys

# Function to safely encode text
def safe_encode(text):
    try:
        return text.encode('utf-8')
    except UnicodeEncodeError:
        # Handling the encoding error
        return text.encode('utf-8', errors='replace')  # Replace problematic characters

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Create the text by safely encoding paragraphs
docText = '\n\n'.join([safe_encode(paragraph.text) for paragraph in document.paragraphs])

# Print the text safely decoded
print(docText.decode("utf-8", errors='replace'))  # Replace errors during decoding
