
import docx

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs directly without encoding
docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Print the text directly since it's already a Unicode string
print(docText)
