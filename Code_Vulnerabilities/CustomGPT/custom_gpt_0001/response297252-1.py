
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Join the paragraphs, ensuring to handle special characters
docText = u'\n\n'.join([
    paragraph.text for paragraph in document.paragraphs])

# Print the text (with proper handling of Unicode)
print docText.encode('utf-8')
