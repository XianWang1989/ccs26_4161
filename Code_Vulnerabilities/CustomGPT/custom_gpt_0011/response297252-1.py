
import docx

# Read the .docx file
document = docx.Document('sim_dir_administrativo.docx')

# Collect the paragraphs in a list and join them with double newlines
docText = '\n\n'.join([
    paragraph.text for paragraph in document.paragraphs
])

# If docText contains any special characters, you can print it directly.
# There might be no need to encode it in utf-8 at this point.
print(docText)
