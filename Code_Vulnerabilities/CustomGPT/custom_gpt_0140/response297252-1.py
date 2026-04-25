
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs directly as Unicode strings
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text (no need to decode as it's already in Unicode)
print(docText.encode('utf-8'))  # Encode only when printing/outputting
