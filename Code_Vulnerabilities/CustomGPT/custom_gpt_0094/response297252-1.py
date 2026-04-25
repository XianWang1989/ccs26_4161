
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Gather text from all paragraphs
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly, ensuring it's encoded properly for output
print docText.encode('utf-8')
