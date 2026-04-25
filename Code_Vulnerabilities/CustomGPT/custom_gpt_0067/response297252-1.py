
import docx

# Read the .docx file
document = docx.Document('sim_dir_administrativo.docx')

# Collect text from paragraphs, joining with double newlines
docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Print the text directly
print(docText)
