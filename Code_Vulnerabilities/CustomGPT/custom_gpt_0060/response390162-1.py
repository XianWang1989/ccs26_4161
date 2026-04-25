
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Example input sentence
sentence = "Adventure movies between 2000 and 2015 featuring performances by Daniel Craig."

# Tokenize and POS-tag the sentence
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Define the chunk grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                    # Chunk for media terms
    RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}           # Chunk for relationships with verbs
    ENTITY: {<NN.*>}                              # Simple entity chunk
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Apply the chunk parser to the tagged tokens
chunked = chunk_parser.parse(tagged_tokens)

# Display the chunking results
print(chunked)
chunked.draw()  # or you can visualize it with .draw() in a GUI environment.
