
import docx

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')

# Join the paragraphs with proper encoding
docText = u'\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Print the text correctly, ensuring it's UTF-8 encoded
print(docText.encode('utf-8'))
