
import docx

# Open the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect paragraphs without encoding at this stage
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Since we're using Python 2.7, print the text directly
# Ensure your terminal or output can handle UTF-8
print docText
