
import nltk
from nltk.chunk import RegexpParser
from nltk import pos_tag, word_tokenize

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize the sentence and tag parts of speech
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define your chunk grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}
  ENTITY: {<NN.*>}
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged points
chunked = chunk_parser.parse(tagged)

# Display the results
print(chunked)

# To visualize the chunking results (optional)
chunked.draw()
