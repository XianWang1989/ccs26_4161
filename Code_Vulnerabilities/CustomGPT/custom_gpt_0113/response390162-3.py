
# Create a parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentence
chunked = chunk_parser.parse(tagged)

# Print the chunked result
print(chunked)
