
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs into a single string
docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Print the text directly (already a Unicode string)
print docText.encode('utf-8')  # Encode for output to handle any special characters
