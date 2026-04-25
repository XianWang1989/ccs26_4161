
import docx

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')

# Collect the text from paragraphs and encode it properly
docText = '\n\n'.join([
    paragraph.text for paragraph in document.paragraphs  # Removed .encode('utf-8')
])

# Print the text directly, since it's already a Unicode string
print docText
