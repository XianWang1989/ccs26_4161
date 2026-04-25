
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect paragraphs as Unicode strings
docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Print the text directly
print docText  # This will correctly handle any Unicode characters
