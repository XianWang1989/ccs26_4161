
import docx

# Load the DOCX file
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs without encoding to UTF-8
docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Print the document text directly
print(docText)
