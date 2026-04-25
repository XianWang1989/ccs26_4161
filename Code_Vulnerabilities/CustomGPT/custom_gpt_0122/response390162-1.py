
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the sentence
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                    # Chunk media phrases
    RELATION: {<V.*><DT>?<JJ>*<NN.*>+}           # Chunk relations followed by NPs
    ENTITY: {<NN.*>}                              # Chunk entities
    """

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentence
result = chunk_parser.parse(tagged)

# Print the chunked result
print(result)

# Optionally visualize the tree structure
result.draw()
