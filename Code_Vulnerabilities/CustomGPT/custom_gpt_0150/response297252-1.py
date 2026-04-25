
import docx

# Open the document
document = docx.Document('sim_dir_administrativo.docx')

# Combine paragraphs into a single Unicode string
docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Now, printing the text directly without decoding
print(docText)
