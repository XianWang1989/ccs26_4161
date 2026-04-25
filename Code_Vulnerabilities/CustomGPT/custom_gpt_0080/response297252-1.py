
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect paragraph texts and join them with newlines, ensuring proper Unicode handling
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly without decoding again
print docText
