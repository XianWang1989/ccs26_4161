
import docx

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')

# Concatenate paragraphs and ensure proper encoding
docText = u'\n\n'.join([
    paragraph.text for paragraph in document.paragraphs])

# Print the text directly, or encode as needed
try:
    print(docText.encode('utf-8'))
except UnicodeEncodeError as e:
    print("Encoding error:", e)
