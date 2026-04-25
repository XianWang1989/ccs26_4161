
# Create a RegexpParser with the defined grammar
chunker = RegexpParser(grammar)

# Apply the chunker to the tagged sentence
chunked_sentence = chunker.parse(tagged_sentence)

# Display the chunked sentence
print(chunked_sentence)
