
import docx

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')

# Create a text variable with proper encoding
docText = u'\n\n'.join([
    paragraph.text for paragraph in document.paragraphs  # Keep it as Unicode
])

# Print the text directly (no need to decode since it's already in Unicode)
print(docText)
