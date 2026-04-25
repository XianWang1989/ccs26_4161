
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Use a list comprehension to create the text, ensuring proper encoding.
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly (no need to encode/decode in Python 2.7 setup)
print docText.decode('utf-8', errors='replace')
