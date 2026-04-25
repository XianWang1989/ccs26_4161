
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Join the paragraphs; no need to encode them
docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Print the document text directly (it's already in Unicode)
print(docText)
