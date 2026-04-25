
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect all paragraph texts, handling any potential encoding issues
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly, which should handle Unicode characters correctly
print(docText)
