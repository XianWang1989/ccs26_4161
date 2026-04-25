
import docx

# Read the DOCX file
document = docx.Document('sim_dir_administrativo.docx')

# Collect the text from the paragraphs and encode correctly
docText = '\n\n'.join([
    paragraph.text for paragraph in document.paragraphs])

# Print the text without manually decoding, since it's already a Unicode string
print(docText.encode('utf-8'))
