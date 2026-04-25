
import docx

# Read the .docx file
document = docx.Document('sim_dir_administrativo.docx')

# Combine the text from the paragraphs without encoding/decoding issues
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly
print(docText)
