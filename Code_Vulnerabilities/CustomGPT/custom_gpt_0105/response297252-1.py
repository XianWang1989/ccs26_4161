
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Read paragraphs and join them directly without encoding
docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Print the document text directly, or handle it as needed
print(docText.encode('utf-8'))  # Encode only when printing or writing
