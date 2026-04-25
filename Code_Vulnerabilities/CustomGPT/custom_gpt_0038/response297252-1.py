
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect paragraphs and encode properly
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text without decoding, as it's already a Unicode string
print docText
