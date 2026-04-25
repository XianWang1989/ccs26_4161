
import docx

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')

# Join the paragraphs directly without encoding
docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Print with appropriate encoding
print docText.encode('utf-8')
