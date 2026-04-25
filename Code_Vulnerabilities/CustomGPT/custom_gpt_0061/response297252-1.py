
import docx

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')

# Join all paragraph texts directly without encoding
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text safely
try:
    print(docText.decode('utf-8'))
except UnicodeDecodeError as e:
    print("Decode Error:", e)

# If you need to encode for specific output (e.g., to a file)
with open('output.txt', 'w') as f:
    f.write(docText.encode('utf-8'))
