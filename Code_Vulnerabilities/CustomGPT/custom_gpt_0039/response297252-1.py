
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs directly as Unicode
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text (or write to a file)
# Make sure to handle potential encoding issues when printing
try:
    print docText.encode('utf-8')
except UnicodeEncodeError as e:
    print("Encoding error:", e)

# If you need to decode later, maintain the original Unicode
# No need to decode at this point if you're using Unicode directly
