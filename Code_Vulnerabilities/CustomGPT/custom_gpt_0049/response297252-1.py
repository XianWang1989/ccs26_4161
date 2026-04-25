
import docx

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')

# Collect the paragraphs as unicode strings
docText = '\n\n'.join([
    paragraph.text for paragraph in document.paragraphs])

# Print the result
print(docText)
