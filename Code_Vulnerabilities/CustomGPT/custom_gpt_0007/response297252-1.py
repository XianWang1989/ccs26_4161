
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Combine paragraphs without immediate encoding to UTF-8
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the document text as is
# Ensure your terminal/console supports Unicode
print docText
