
import docx

# Read the DOCX file
document = docx.Document('sim_dir_administrativo.docx')

# Collect the text from paragraphs, maintaining Unicode
docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Print the collected text directly
print(docText)  # No need to encode/decode as it's already Unicode
