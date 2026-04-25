
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample phrase
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag
words = word_tokenize(text)
tagged = pos_tag(words)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}
  ENTITY: {<NN.*>}
  PP: {<IN><MEDIA|ENTITY>}
  VP: {<V.*>(<MEDIA|ENTITY|PP>)*}
  CLAUSE: {<NP><VP>}
"""

# Initialize the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentence
chunked = chunk_parser.parse(tagged)

# Print the results
print(chunked)
chunked.draw()
