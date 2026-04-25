
# Define cascaded grammar
cascaded_grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                # Media entities
    RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}       # Relationships
    ENTITY: {<NN.*>}                           # General entities
"""

# Create the first chunk parser
media_parser = RegexpParser(cascaded_grammar)

# First chunk
media_chunk = media_parser.parse(tagged_tokens)

# Now you can analyze media_chunk further if necessary
print("First Layer Chunking:")
print(media_chunk)

# You can create additional parsing as needed; for example, to find relations within the chunks
relation_chunk = media_parser.parse(media_chunk)

print("\nSecond Layer Chunking:")
print(relation_chunk)
