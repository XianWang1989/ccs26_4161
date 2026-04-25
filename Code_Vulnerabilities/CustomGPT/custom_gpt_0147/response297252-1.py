
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs into a single string
docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Print the text directly
print(docText)  # This should work without decoding issues
