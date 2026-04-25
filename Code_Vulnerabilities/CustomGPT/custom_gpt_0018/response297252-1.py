
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Concatenate the paragraphs with "\n\n" and encode them directly in UTF-8
docText = '\n\n'.join([
    paragraph.text for paragraph in document.paragraphs])

# Print the text directly without decoding since it's already a string
print(docText.encode('utf-8'))
