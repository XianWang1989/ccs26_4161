
# Sample text
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig directed by sam mendes"

# Tokenize and POS tag the text
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)

# Create and apply the chunk parser
chunk_parser = RegexpParser(grammar)
chunks = chunk_parser.parse(pos_tags)

print("Chunked Output:")
print(chunks)
