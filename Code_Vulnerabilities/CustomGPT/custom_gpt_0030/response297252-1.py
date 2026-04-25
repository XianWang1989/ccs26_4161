
import docx

# Read the .docx file
document = docx.Document('sim_dir_administrativo.docx')
# Join paragraphs into a single string, keeping it as a Unicode string
docText = u'\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# If you want to print the text, you can print it directly
print docText

# If you need to encode it for output or saving
with open('output.txt', 'w') as f:
    f.write(docText.encode('utf-8'))  # Encode when writing to a file
