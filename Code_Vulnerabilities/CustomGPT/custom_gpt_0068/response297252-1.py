
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Concatenate paragraphs into a single string, ensuring encoding is handled
docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Since we're using Python 2.7, we should encode the output to display it correctly
try:
    # Print the document text (if necessary encode it for the terminal)
    print(docText.encode('utf-8'))  # Encode to UTF-8 for terminal output
except UnicodeEncodeError as e:
    print("Encoding error:", e)

# If you need to decode it, do it as follows (but usually you just print the necessary string)
# docText_decoded = docText.decode('utf-8')  # This may not be necessary for terminal output
