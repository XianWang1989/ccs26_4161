
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect paragraphs and ensure proper handling of unicode
docText = '\n\n'.join([
    paragraph.text for paragraph in document.paragraphs])

# Print the text directly since we are in a Unicode context
print(docText)
