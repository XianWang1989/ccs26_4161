
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect paragraphs as a single string with proper encoding
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly, since it should already be a Unicode string
print(docText)
