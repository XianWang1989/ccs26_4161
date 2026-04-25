
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Define your grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}
    RELATION: {<V.*><DT>?<JJ>*<NN.*>+}
    ENTITY: {<NN.*>}
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Tokenize and tag
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Chunk the tagged tokens
chunks = chunk_parser.parse(tagged)

# Display the results
print(chunks)
