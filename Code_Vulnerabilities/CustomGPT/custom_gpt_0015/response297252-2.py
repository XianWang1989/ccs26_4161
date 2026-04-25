
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(docText.encode('utf-8'))  # Ensure to encode when writing to a file
