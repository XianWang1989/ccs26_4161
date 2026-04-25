
import nltk
from nltk.chunk import RegexpParser
from nltk import pos_tag, word_tokenize

# Sample text
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the text
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define the grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}
    RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}
    ENTITY: {<NN.*>}
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged text
chunks = chunk_parser.parse(tagged)

# Display the resulting chunks
print(chunks)

# Optionally, to visualize the chunks
chunks.draw()
